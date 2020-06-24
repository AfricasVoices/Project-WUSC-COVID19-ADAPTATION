#!/usr/bin/env bash

set -e

if [[ $# -ne 3 ]]; then
    echo "Usage: ./1_coda_get.sh <coda-auth-file> <coda-v2-root> <data-root>"
    echo "Downloads coded messages datasets from Coda to '<data-root>/Coded Coda Files'"
    exit
fi

AUTH=$1
CODA_V2_ROOT=$2
DATA_ROOT=$3

./checkout_coda_v2.sh "$CODA_V2_ROOT"
cd "$CODA_V2_ROOT/data_tools"
git checkout "9a9a8e708e3f20f37848a6b02f79bcee43e5be3b"  # (master which supports segmenting)

mkdir -p "$DATA_ROOT/Coded Coda Files"

PROJECT_NAME="WUSC-COVID19-ADAPTATION"
DATASETS=(
    "dadaab_s01e01"
    "dadaab_s01e02"
    "dadaab_s01e03"
    "dadaab_s01e04"
    "dadaab_s01e05"
    "dadaab_s01e06"
    "dadaab_s01e07"
    "dadaab_s01e08"
    "dadaab_s01e09"
    "dadaab_s01e10"
    "dadaab_learning_from_home_experience"
)

for DATASET in ${DATASETS[@]}
do
    echo "Getting messages data from ${PROJECT_NAME}_${DATASET}..."

    pipenv run python get.py "$AUTH" "${PROJECT_NAME}_${DATASET}" messages >"$DATA_ROOT/Coded Coda Files/$DATASET.json"
done
PROJECT_NAME="WUSC-KEEP-II"
DATASETS=(
    "dadaab_location"
    "dadaab_gender"
    "dadaab_age"
    "dadaab_nationality"
    "dadaab_household_language"
)

for DATASET in ${DATASETS[@]}
do
    echo "Getting messages data from ${PROJECT_NAME}_${DATASET}..."

    pipenv run python get.py "$AUTH" "${PROJECT_NAME}_${DATASET}" messages >"$DATA_ROOT/Coded Coda Files/$DATASET.json"
done
