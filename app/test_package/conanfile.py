import os

from conan import ConanFile
from conan.tools.build import can_run


class StuffTestPkg(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "VirtualRunEnv"

    def requirements(self):
        self.requires(self.tested_reference_str, run=True)

    def test(self):
        if can_run(self):
            self.run("stufftool", env="conanrun")
        self.output.success("stuff package test OK.")
