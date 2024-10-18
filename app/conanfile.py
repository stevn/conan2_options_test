import os

from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.files import copy
from conan.tools.build import can_run


COMPONENT_STUFF_TOOL = "stufftool"

class StuffToolConanPkg(ConanFile):

    name = "stufftool"
    version = "1.0.0"

    package_type = "application"

    settings = "os", "compiler", "build_type", "arch"

    exports_sources = "CMakeLists.txt", "src/*"

    tool_requires = "cmake/[^3]"

    generators = [
        "CMakeDeps",
        "CMakeToolchain",
        "VirtualBuildEnv",
        "VirtualRunEnv",
    ]

    def requirements(self):
        self.requires('opencv/4.10.0')
        self.requires('stuff/1.0.0')

    def configure(self):
        self.options["opencv"].with_ffmpeg = False

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        if can_run(self):
            cmake.test()

    def package(self):
        if self.settings.os == "Windows":
            copy(self,
                pattern="*/stufftool.exe",
                src=self.build_folder,
                dst=os.path.join(self.package_folder, 'bin'),
                keep_path=False,
            )
            copy(self,
                pattern="*/stufftool.pdb",
                src=self.build_folder,
                dst=os.path.join(self.package_folder, 'bin'),
                keep_path=False,
            )
        else:
            copy(self,
                pattern="*/stufftool",
                src=self.build_folder,
                dst=os.path.join(self.package_folder, 'bin'),
                keep_path=False,
            )

    def package_info(self):
        self.cpp_info.components[COMPONENT_STUFF_TOOL].requires = [
            "stuff::stuff",
            "opencv::opencv",
        ]
