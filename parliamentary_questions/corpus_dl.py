import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np 
import math, os, sys 
from log.logger import Logger, LogLevel
logger = Logger(LogLevel.DEBUG)

# Corpus DL
from convokit import Corpus
from convokit import download

DATA_DIR : str = "PARL_DATA/"
CORPUS : str = "parliament-corpus"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--dl":
            logger.info(f"downloading corpus to {DATA_DIR}")
            PARL_CORPUS_PATH : str = download(
                CORPUS,
                data_dir=DATA_DIR
            )
    try:
        logger.info(f"Loading {DATA_DIR}{CORPUS}...")
        parl_corpus = Corpus(DATA_DIR + CORPUS)
        parl_corpus.print_summary_stats()
    except Exception as e:
        logger.error(f"error loading corpus: {str(e)}")
        logger.debug("run with -dl first?")
