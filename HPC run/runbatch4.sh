#!/bin/bash
#BSUB -J Batch1
#BSUB -q gpuv100
#BSUB -R "rusage[mem=32GB]"
#BSUB -B
#BSUB -N
##BSUB -u esbenyo@gmail.com
#BSUB -o Output_%J.out
#BSUB -e Output_%J.err
#BSUB -W 1:00
#BSUB -n 8
#BSUB -R "span[hosts=1]"
#BSUB -gpu "num=2:mode=exclusive_process"

source ~/miniconda3/etc/profile.d/conda.sh
conda activate base
module load cuda/11.8
 
# Starts llama.cpp server
~/dtu/blackhole/03/225731/llama.cpp/build/bin/llama-server \
    -m ~/dtu/blackhole/03/225731/llama.cpp/qwen3-235b-q4/Qwen3-235B-A22B-Q4_K_M.gguf \
    --host 127.0.0.1 \
    --port 11434 &
 
# Waits until the server and model are fully loaded
echo "Waiting for llama-server to start..."
until curl -s http://127.0.0.1:11434/health | grep -q '"status":"ok"'; do
    sleep 2
done
echo "Server is up, starting batch jobs..."
 
python3 batch1.py > joboutput_batch1_$LSB_JOBID.out 2>&1
 
# Shuts down the server
kill %1
