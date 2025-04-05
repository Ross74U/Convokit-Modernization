import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np 
import math, os

# Corpus DL
from convokit import Corpus
from convokit import download

DATA_DIR : str = "PARL_DATA"
PARL_CORPUS_PATH : str = download('parliament-corpus', data_dir=DATA_DIR)

print(PARL_CORPUS_PATH)
parl_corpus = Corpus(PARL_CORPUS_PATH)
parl_corpus.print_summary_stats()
