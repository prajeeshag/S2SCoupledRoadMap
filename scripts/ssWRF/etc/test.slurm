#!/bin/bash
#SBATCH -N 1
#SBATCH --ntasks=10
#SBATCH --partition=debug
#SBATCH --exclusive
#SBATCH --cpus-per-task=1
###SBATCH --mem-per-cpu=4G


echo "Start testing"

for i in {1..50}; do
  srun --ntasks=1 --mem=0 --exclusive ./test_run.sh $i &
done
wait