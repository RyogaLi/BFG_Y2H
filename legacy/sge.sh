#!/bin/bash

# script for submitting jobs to sge cluster
# each cluster takes two fastq files, r1 and r2

#FASTQ=$1
#OUTPUT=$2

# getopts

while getopts ":f:o:m:" opt; do
  case $opt in 
    f) FASTQ="$OPTARG"
      ;;
    o) OUTPUT="$OPTARG"
      ;;
    m) MODE="$OPTARG"
      ;;
    \?) echo "Invalid option -$OPTARG" >&2
  esac
done

printf "Reading fastq files from %s\n" "$FASTQ"
printf "The output will be saved to %s\n" "$OUTPUT"
printf "Mode %s\n" "$MODE"

# create the directory and run script
# attention: if outpur dir exists it will be removed
#rm -r $OUTPUT; mkdir $OUTPUT
if [[ ! -z "${FASTQ// }" ]]; then
  for fastq in $FASTQ/*_R1_*.fastq.gz; do
    echo $fastq
    echo "here"
  # get AD and DB group info from file name

  #/home/rothlab/rli/py/bin/python2.7 ./bfg_analysis/main.py --fastq $fastq --output $OUTPUT
  qsub -l "h_vmem=40G" -N $(basename $fastq .fastq.gz) ./sge_sub.sh $fastq $OUTPUT $MODE
done
fi

exit 1

# check # jobs running
i=1
while [ $i -eq 1 ]; do
  # change user name here
  COMMAND=$(qstat -u rli |wc -l)
  echo "Total jobs running... : "$COMMAND # DEBUG MEG
  if [ $COMMAND -eq 0 ]; then
    echo "Starting score optimizations ... "
    ##iiii=0
    for sample in $OUTPUT*; do
      echo $sample
      #FULLPATH=$(pwd $OUTPUT)/$sample/
      #echo $FULLPATH
      #pre=$sample"_pre"$matrix
      #med=$sample"_med"$matrix
      #high=$sample"_high"$matrix
      qsub -N $(basename $sample) ./sge_score_sub.sh $sample
      #/home/rothlab/rli/py/bin/python2.7 ./bfg_analysis/score.py --sample $sample
    done
    i=0
  else
    sleep 1800
  fi
done
