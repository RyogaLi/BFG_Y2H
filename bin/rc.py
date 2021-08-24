#!/usr/bin/env python3.7
import argparse
from bfg_analysis import read_counts
# Author: Roujia Li
# email: Roujia.li@mail.utoronto.ca
parser = argparse.ArgumentParser(description='BFG-Y2H')

# make fasta from summary file (AD and DB)
# -- create: creates fasta file from summary.csv
# parser.add_argument('--pfasta', help="Path to fasta file")

# parameters for cluster
parser.add_argument("-r1", help="Read 1 SAM file")
parser.add_argument("-r2", help="Read 2 SAM file")
parser.add_argument("--AD_GROUP", help="AD group number")
parser.add_argument("--DB_GROUP", help="DB group number")
parser.add_argument("--mode", help="Mode (yeast, human, virus, hedgy)")
parser.add_argument("--cutoff", help="SAM reads quality cutoff", type=int)
parser.add_argument("--summary", help="path to all summary files", default="/home/rothlab/rli/02_dev/08_bfg_y2h/bfg_data/summary/")
parser.add_argument("-o", "--output", help="Output path")
args = parser.parse_args()

read_counts.RCmain(args.r1, args.r2, args.AD_GROUP, args.DB_GROUP, args.mode, args.output, args.cutoff, args.summary)
