from typing import Dict, List, Any 
import time

import umap
from log.logger import Logger, LogLevel
logger = Logger(LogLevel.DEBUG)

# Corpus DL
DATA_DIR : str = "PARL_DATA/"
CORPUS : str = "parliament-corpus"

def load_corpus(attribute : str = "utterances", n: int = 1000) -> List[Dict]:
    import json
    data : List[Dict] = []
    file_path = DATA_DIR + CORPUS + "/" + attribute + ".jsonl"
    with open(file_path, 'r', encoding='utf-8') as f:
        i = 0
        for line in f:
            if i > n:
                break
            if line.strip():  # Skip empty lines
                data.append(json.loads(line))
            i+=1

    return data

if __name__ == "__main__":
    '''
    try:
        parl_corpus = Corpus(DATA_DIR + CORPUS)
        parl_corpus.print_summary_stats()
    except Exception as e:
        logger.error(f"error loading corpus: {str(e)}")
        logger.debug("run with -dl first?")
        sys.exit(-1)
    '''
    n : int = 3000


    # do we load utterances directly or a specialized arc, we want to capture
    # contexual information directly in the embeddings so let's do utterances
    
    logger.info(f"Loading {DATA_DIR}{CORPUS}...")
    t1 = time.perf_counter()
    corpus : List[Dict] = load_corpus('utterances', n) # note: 398 MB of jsonl data
    t2 = time.perf_counter()
    logger.info(f"corpus loaded in {t2-t1}!")
    

    # implement convokit approach
    # actually I don't think we need to just yet, they did it for us
    # https://github.com/CornellNLP/ConvoKit/blob/master/convokit/expected_context_framework/demos/parliament_demo.ipynb


    logger.info("loading SBERT Model")
    from sentence_transformers import SentenceTransformer
    sbertmodel = SentenceTransformer("sentence-transformers/paraphrase-mpnet-base-v2", device="cuda")
    logger.info("loaded!")

    logger.info("Loading UMAP dim reduction")
    reducer = umap.UMAP(
        n_components=2,
        n_neighbors=15,
        min_dist=0.1,
        metric='cosine',
        low_memory=False,
        random_state=42
    )
    embeddings : List[Any] = []

    for i in range(0,n):    
        t1 = time.perf_counter()
        embedding = sbertmodel.encode(corpus[i]["text"])
        embeddings.append(embedding)
        t2 = time.perf_counter()
        logger.info(f"Tensor Shape : {embedding.shape}")
        logger.info(f"embedding computed in {(t2-t1)*1000.0} ms")

    logger.info(f"reducing dimensions using umap")
    reduced_embeddings = reducer.fit_transform(embeddings)
    
######################## PLOTTING #####################
    import matplotlib.pyplot as plt
    import numpy as np
    from sklearn.cluster import HDBSCAN
    import seaborn as sns

    logger.info(f"clustering")
    clusterer = HDBSCAN(
        min_cluster_size=5,    # Minimum size of a cluster
        min_samples=5,          # More conservative clustering with higher values
        metric='euclidean',     # Use Euclidean for the 2D UMAP space
        cluster_selection_method='eom'  # Excess of Mass
    )
    cluster_labels = clusterer.fit_predict(reduced_embeddings)

    plot_embeddings = np.array(reduced_embeddings)

# 4. Create a colorful visualization with continuous coloring
    plt.figure(figsize=(12, 10))

# Set up a good color palette (using a colormap with good perceptual separation)
    distinct_colors = sns.color_palette("hls", len(set(cluster_labels)))
    colors = [distinct_colors[label] if label != -1 else (0.8, 0.8, 0.8) for label in cluster_labels]

# Create scatter plot with colored points
    scatter = plt.scatter(
        plot_embeddings[:, 0], 
        plot_embeddings[:, 1], 
        c=colors,
        s=50,             # Point size
        alpha=0.8,        # Transparency
        edgecolors='none'
    )

# Add annotations for cluster centers

    plt.tight_layout()
    plt.show()
