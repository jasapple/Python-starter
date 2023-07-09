#!/usr/bin/env python3
"""
Author: Joshua Singh

"""
import argparse
import logging
import time

logging.basicConfig(format='%(asctime)s [%(levelname)s] - %(message)s', datefmt='%Y-%m-%dT%H:%M:%S %Z')
logging.Formatter.converter = time.gmtime
logger = logging.getLogger()
logger.setLevel(logging.ERROR)

def main():
    exit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Cool script description here.')
    parser.add_argument("-v", "--verbose", action="count", default=0, help="increase output verbosity")
    parser.add_argument('-l', '--log', type=str, help='Path to log file')

    args = parser.parse_args()

    if args.verbose > 0:
        logger.setLevel(logging.INFO)

        if args.verbose > 1:
            logger.setLevel(level=logging.DEBUG)

        if args.log:
            logger.addHandler(logging.FileHandler(filename=args.log, filemode='a'))

        logger.info("args passed: " + str(args))
   
    try:
        main()
    except (Exception):
        logger.error(exc_info=True)
