# Current framework of realtime transcriptional understanding: 2 Extremes
## One end: Convokit, built specifically for conversation / large scale corpus processing for conversational understanding, generally predates modern LLM and sentence-transformer
https://convokit.cornell.edu/documentation/featureExtraction.html
- [ ] Bag-of-words
- [ ] Column-normalized tf-idf
- [ ] Hyperconvo
- [ ] PhrasingMotifs
- [ ] PolitenessStrategies
- [ ] PromptTypes
- [ ] ExpectedContextModel*

### Example: ExpectedContextModel - approach based on contextual understanding of utterances in context
 - based on LSA approach combined with SVD reduction in dimension
- it models utterances based on their conversational context - specifically how they relate to replies and predecessors in conversations. The model embeds terms and utterances in a latent "context space" where proximity indicates similarity in expected conversational role/function rather than just semantic similarity.
 - They use Latent Semantic Analysis (LSA) to create these embeddings, applying SVD to matrices representing utterance-term and context-term relationships. This creates a shared vector space for terms, utterances and contexts.
 - The focus is on modeling the expected conversational flow and function, not just semantic content. For example, two questions might be embedded close together if they tend to elicit similar types of answers, even if they're about different topics.

#### Key: good for certain tasks (understanding redirection (SCOTUS), therapy, and other tasks in which conversational flow and nuisances are more important than semantics), highly performant (built for large corpus). Lacks in versatility, specific domain specific application

The other approaches mentioned above are simpler, often highly performant, yet are very specific and unable to be easily adapted for general use


## the other end: Instructor LLM based approach - Naiive. Highly general, but high resource consumption, often centralized. Understanding complex text requires very large models practically only available as APIs from large providers such as OpenAI, Anthripic, Google, Meta, etc.
 - prompt engineering approach
 - Current example usage: Current startup providing telephone agents for client information (Swartz center)
 - Current example usage: LLM social media comment analysis/filtering. Overlaps with convokit framework: analysis of Reddit comments to predict certain conversational features (using bag of words)


# Proposal: SBERT-based transformer for realtime contextual, semantic, conversational understanding 
- Generally adaptable to many situations requiring realtime understanding
    - bidirectional context understanding
    - semantic and topic relation understanding
- Much higher performance than LLM prompt engineering approach
    - able to be distributed: computation can feasilbly run on personal computers, applicable for decentralized computation
- higher quality and general adaptability than convokit ensemble approach

# Realtime performance measures
1. Convokit Framework (ExpectedContextModel):
Factors:
- LSA + SVD computation is relatively lightweight
- No deep learning models involved
- Primarily matrix operations
- Pre-computed embeddings can be reused
Expected Latency: ~10-50ms per utterance
- Matrix operations are fast on CPU
- Most computation can be vectorized,well-optimized

2. LLM Prompt Engineering Approach:
Factors:
- Requires API call to external service
- Network latency
- Large model inference time
- Token processing overhead
Expected Latency: ~500-2000ms per utterance depending on network availability and chosen model
- Model inference: ~400-1800ms

3. SBERT-based Transformer:
Factors:
- Local computation possible
- Optimized for sentence embeddings
- Can run on CPU or GPU
Expected Latency: ~50-200ms per utterance
- Model inference: ~40-150ms
- Embedding computation: ~10-50ms
- Can be optimized further with batching

These metric estimates assume:
- Standard hardware (modern CPU/GPU) - SBERT was run on Nvidia RTX 5000 12GB vram (not optmized), LSA run on intel i7-9750H
- naiive LLM baseline measured with standard OpenAI API endpoint with GPT-3.5 Turbo Instructor model (200 token limit per utterance, periods of low and high traffic)
- Average utterance length (~20-50 words)
- No extreme optimization
- Single utterance processing (not batch)

The SBERT approach offers a good middle ground between Convokit's high performance but limited flexibility and LLM's high flexibility but poor latency. It provides reasonable latency while maintaining adaptability for various conversational understanding tasks.

# Currently conducting  
Evaluation of SBERT approach against convokit on convokit home stadium (expected context, predicted conversational flow, redirection) using Corpuses (originally compiled for convokit)
# Next step
Evaluation of SBERT approach against naiive LLM prompt engineering approach


# Specific Measures: Known examples in Convokit
Analysis of Parliamentary Question Periods
