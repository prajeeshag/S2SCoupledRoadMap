#!/bin/bash
# For ECMWF Forecast files
# Files: FORE.yyyymmdd.0, SURF.yyyymmdd.0
#        FORE.yyyymmdd, SURF.yyyymmdd (Ensembles) 
#

IDIR=$1
DATE=${2}
DATE=${DATE:0:8} #yyyymmdd
MAXENS=$3
ODIR=$4

WGRIB=${WGRIB:=wgrib}

for fprfx in FORE SURF; do
  ifile="$IDIR/$fprfx.$DATE.0"
  cp $ifile $ODIR/
done

#exit succefully if MAXENS==1
if [ "$MAXENS" -eq 1 ]; then
    exit 0
fi

MAXENS=$((MAXENS-1))
for fprfx in FORE SURF; do
  ifile="$IDIR/$fprfx.$DATE"
  ${WGRIB:=wgrib} -s $ifile > inv
  n_ens=$(cat inv | awk -F":" '{print $(NF-1)}' | sort | uniq | wc -l)
  if [ "$MAXENS" -gt "$n_ens" ]; then
    echo "ERROR: There isn't enough ensemble members in the input files!!" >&2
    exit 1
  fi
  for ((i=1;i<=$MAXENS;i++)); do
    ofile="${ODIR}/$fprfx.$DATE.$i"
    grep "Perturbed forecast $i:" < inv | $WGRIB -i $ifile -s -grib -o $ofile > /dev/null
  done
done

rm inv
