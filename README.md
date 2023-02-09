# onnx-custom

## Prerequisite

- libtorch Release CPU version (1.12.0)
    - **Tested on CPU.** / CUDA is planned
- WSL2 (**for Linux**)
- Clang 10+ (**for Linux**)
- PyTorch 1.12+ (**for Linux and Windows**)
- onnx 1.12.0+ (**for Linux and Windows**)
- onnxruntime 1.13.1 (**for Linux and Windows**)
- onnxruntime-extensions 0.5.0(**for Windows**)
- onnxruntime-extensions 0.4.2(**for Linux**)

## How to execute 
1. [Cmake 설치](https://cmake.org/download/)

- 1.1 VScode의 CMake, CMake Language Support, CMake Tools 설치

- 1.2 WSL 접속 (VS code 추천)

- 1.3 CMakeLists.txt를 저장 [(LibTorch 저장 경로 수정 필요)](https://github.com/kaintels/onnx-custom/blob/main/CMakeLists.txt#L9-L10)

- 1.4 ```python setup.py install``` (in Linux OS)

- 1.5 ```python model_export.py``` (in Linux OS)

- 1.6 ```python inference.py``` (in Linux / Windows OS)