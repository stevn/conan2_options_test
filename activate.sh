set -e

if [ "$(uname)" == "Darwin" ]; then
    echo "Activating macOS environment..."

    # Conan v2 home dir.
    export CONAN_HOME=$(pwd)/.conan2_mac

    if [[ $1 == new ]]; then
        conan profile detect --exist-ok --name default
        touch $CONAN_HOME/global.conf
        truncate -s 0 $CONAN_HOME/global.conf
        echo jbig/*:tools.cmake.cmaketoolchain:generator=DummyGeneratorToPreventBuildingOfJBIG >> $CONAN_HOME/global.conf
    fi

elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    echo "Activating Linux environment..."

    # Conan v2 home dir.
    export CONAN_HOME=$(pwd)/.conan2_linux

    if [[ $1 == new ]]; then
        conan profile detect --exist-ok --name default
        touch $CONAN_HOME/global.conf
        truncate -s 0 $CONAN_HOME/global.conf
        echo jbig/*:tools.cmake.cmaketoolchain:generator=DummyGeneratorToPreventBuildingOfJBIG >> $CONAN_HOME/global.conf
        echo tools.system.package_manager:mode=install >> $CONAN_HOME/global.conf
    fi

else
    echo "Unknown OS."
fi

echo "Env OK."
