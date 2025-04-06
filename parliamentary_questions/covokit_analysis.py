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
    try:
        logger.info(f"Loading {DATA_DIR}{CORPUS}...")
        parl_corpus = Corpus(DATA_DIR + CORPUS)
        parl_corpus.print_summary_stats()
    except Exception as e:
        logger.error(f"error loading corpus: {str(e)}")
        logger.debug("run with -dl first?")
        sys.exit(-1)

    parl_corpus.load_info('utterance',['arcs','q_arcs'])
