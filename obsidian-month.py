import sys
import argparse
parser = argparse.ArgumentParser(description= 'file generator')
parser.add_argument('-n', action='store', dest='n', help='Simple value')
args = parser.parse_args()
