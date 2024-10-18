import os

from conan import ConanFile
from conan.tools.build import can_run
from conan.tools.cmake import CMake, cmake_layout


class StuffLibTestPkg(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain", "VirtualBuildEnv", "VirtualRunEnv"
    tool_requires = "cmake/[^3]"

    def requirements(self):
        self.requires(self.tested_reference_str)

    def layout(self):
        """Specify file layout of the package."""
        cmake_layout(self)

    def build(self):
        """Build the package (runs CMake configure, build, test)."""
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if can_run(self):
            self.run(os.path.join(self.cpp.build.bindirs[0], "stufflibtestpkg"), env="conanrun")
        self.output.success("stufflib package test OK.")
