#!/bin/bash -e

cd $(dirname "$0")
for i in expr_*.py; do
    (set -x; python3 $i)
done
