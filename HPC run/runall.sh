#!/usr/bin/env bash

set -euo pipefail

for i in {1..10}; do
    bsub < "runbatch{i}.sh"
done