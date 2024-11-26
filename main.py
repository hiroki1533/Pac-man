import os
import argparse
from config import common_args, Parameters
from utils import dump_params, setup_params
from utils import set_logging
import logging
from game import Game

if __name__ == "__main__":
    params = Parameters()
    game = Game(params)
    game.start()
