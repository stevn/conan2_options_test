source activate.sh
git clean -fx -e ".conan*" .
conan remove "stuff*" -c
conan remove "jbig" -c
