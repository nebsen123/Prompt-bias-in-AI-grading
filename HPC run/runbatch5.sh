#!/bin/bash
#BSUB -J Batch1gptoss1GPU3Test
#BSUB -q gpua100
#BSUB -R "rusage[mem=4GB]"
#BSUB -R "select[gpu80gb]"
#BSUB -B
#BSUB -N
##BSUB -u esbenyo@gmail.com
#BSUB -o Output_%JBatch5.out
#BSUB -e Output_%JBatch5.err
#BSUB -W 2:00
#BSUB -n 8
#BSUB -R "span[hosts=1]"
#BSUB -gpu "num=1:mode=exclusive_process"

source ~/miniconda3/etc/profile.d/conda.sh
conda activate base
module load cuda/11.8
 
# Starts llama.cpp server
/dtu/blackhole/03/225731/llama.cpp/build/bin/llama-server \
  -m /dtu/blackhole/03/225731/llama.cpp/myModels/gpt-oss-120b/gpt-oss-120b-mxfp4-00001-of-00003.gguf \
  --split-mode layer\
  -ngl all \
  --host 127.0.0.1 \
  --port 11434 &

LLAMA_PID=$!
trap 'kill "$LLAMA_PID" 2>/dev/null || true' EXIT
 
# Waits until the server and model are fully loaded
echo "Waiting for llama-server to start..."
until curl -s http://127.0.0.1:11434/health | grep -q '"status":"ok"'; do
    sleep 2
done
echo "Server is up, starting batch jobs..."
 
python3 batch5.py > joboutput_batch5_$LSB_JOBID.out 2>&1
 
# Shuts down the server
kill "$LLAMA_PID" 2>/dev/null || true
wait "$LLAMA_PID" 2>/dev/null || true