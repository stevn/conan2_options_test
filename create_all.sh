set -e

source activate.sh new

pushd lib
conan create . --build missing
popd

pushd app
conan create . --build missing
popd

echo "Checking if JBIG was built automatically (which we *DO NOT* want)..."
conan list jbig
