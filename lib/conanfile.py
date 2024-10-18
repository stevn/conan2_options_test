import os

from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.files import copy


COMPONENT_STUFF_LIB = "stuff"


class StuffLibConanPkg(ConanFile):

    name = "stuff"
    version = "1.0.0"

    package_type = "library"

    settings = "os", "compiler", "build_type", "arch"

    options = {
        "shared": [True, False],
    }
    default_options = {
        "shared": False,
    }

    exports_sources = "CMakeLists.txt", "src/*"

    tool_requires = "cmake/[^3]"

    generators = [
        "CMakeDeps",
        "CMakeToolchain",
        "VirtualBuildEnv",
        "VirtualRunEnv",
    ]

    def requirements(self):
        self.requires('libtiff/4.6.0')

    def configure(self):
        # Force disable JBIG because it is GPL licensed.
        self.options["libtiff"].jbig = False

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        copy(self,
            pattern="*",
            src=os.path.join(self.source_folder, 'src/include'),
            dst=os.path.join(self.package_folder, 'include'),
        )
        copy(self,
            pattern="*/stuff_export.h",
            src=os.path.join(self.build_folder),
            dst=os.path.join(self.package_folder, 'include'),
            keep_path=False,
        )
        if self.settings.os == "Windows":
            copy(self,
                pattern="*/stuff.lib",
                src=self.build_folder,
                dst=os.path.join(self.package_folder, 'lib'),
                keep_path=False,
            )
            copy(self,
                pattern="*/stuff.dll",
                src=self.build_folder,
                dst=os.path.join(self.package_folder, 'bin'),
                keep_path=False,
            )
            copy(self,
                pattern="*/stuff.pdb",
                src=self.build_folder,
                dst=os.path.join(self.package_folder, 'bin'),
                keep_path=False,
            )
        else:
            copy(self,
                pattern="*/libstuff.a",
                src=self.build_folder,
                dst=os.path.join(self.package_folder, 'lib'),
                keep_path=False,
            )
            copy(self,
                pattern="*/libstuff.dylib",
                src=self.build_folder,
                dst=os.path.join(self.package_folder, 'lib'),
                keep_path=False,
            )

    def package_info(self):
        self.cpp_info.components[COMPONENT_STUFF_LIB].libs = [COMPONENT_STUFF_LIB]
        self.cpp_info.components[COMPONENT_STUFF_LIB].includedirs = ['include']
        self.cpp_info.components[COMPONENT_STUFF_LIB].requires = [
            'libtiff::libtiff',
        ]
