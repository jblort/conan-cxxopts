from conans import ConanFile, CMake, tools


class CxxoptsConan(ConanFile):
    name = "cxxopts"
    version = "2.1.1"
    license = "MIT"
    url = "https://github.com/jblort/conan-cxxopts"
    description = "This is a lightweight C++ option parser library, supporting the standard GNU style syntax for options."
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def source(self):
        self.run("git clone --depth 1 --branch v2.1.1 https://github.com/jarro2783/cxxopts")
        self.run("cd cxxopts")
        # This small hack might be useful to guarantee proper /MT /MD linkage in MSVC
        # if the packaged project doesn't have variables to set it properly
        tools.replace_in_file("cxxopts/CMakeLists.txt", "project(cxxopts)", '''project(cxxopts)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir="%s/cxxopts" % self.source_folder)

    def package(self):
        self.copy("cxxopts.hpp", dst="include", src="cxxopts/include")
