import argparse


def get_args():
    parser = argparse.ArgumentParser('logger')
    parser.add_argument('-s', action='store_true')
    parser.add_argument('-f', action='store_true')
    return parser.parse_args()
