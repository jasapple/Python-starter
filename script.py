#!/usr/bin/env python3
"""
Author: Joshua Singh

"""
import argparse
import logging
import time
import os

logger = None

def main():
    exit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Cool script description here.')
    parser.add_argument("-v", "--verbose", action="count", help="increase output verbosity")
    parser.add_argument('-l', '--log', type=str, help='Path to log file')

    args = parser.parse_args()

    if args.verbose > 0:
        logging.basicConfig(format='%(asctime)s [%(levelname)s] - %(message)s', datefmt='%Y-%m-%dT%H:%M:%S %Z')
        logging.Formatter.converter = time.gmtime
        if args.log:
            logging.basicConfig(filename=args.log, filemode='a')

        if args.verbose > 1:
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.INFO)

        logger = logging.getLogger()

        logger.info("args passed: " + str(args))
   
    try:
        main()
    except (Exception) as e :
        logger.error(e)
