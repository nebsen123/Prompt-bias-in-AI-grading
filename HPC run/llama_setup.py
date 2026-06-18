# we downloaded the llama.cpp git to the HPC with these commads

git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp

# we then built the project with these

cmake -B build -DGGML_CUDA=ON
cmake --build build --config Release

# to find a more in depth guide on how to install the llama.cpp project look here: https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md#cpu-build

#we then downloaded our model with these commands:
wget -c https://huggingface.co/ggml-org/gpt-oss-120b-GGUF/resolve/main/gpt-oss-120b-mxfp4-00001-of-00003.gguf
wget -c https://huggingface.co/ggml-org/gpt-oss-120b-GGUF/resolve/main/gpt-oss-120b-mxfp4-00002-of-00003.gguf
wget -c https://huggingface.co/ggml-org/gpt-oss-120b-GGUF/resolve/main/gpt-oss-120b-mxfp4-00003-of-00003.gguf
#a guide on how to download and credits can be found here: https://huggingface.co/ggml-org/gpt-oss-120b-GGUF/tree/main

# to test if the model was set up correctly we ran this command:
./build/bin/llama-cli \
  -m myModels/gpt-oss-120b/gpt-oss-120b-mxfp4-00001-of-00003.gguf \
  --jinja \
  -ngl 20 \
  -p "Hej, virker modellen?"