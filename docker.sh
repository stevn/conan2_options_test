set -e
docker buildx build -t conan_options_test .
docker run --rm -it -v `pwd`:/workspace -w /workspace conan_options_test
