cmake_minimum_required(VERSION 3.26)

set(CMAKE_CXX_VISIBILITY_PRESET hidden)
set(CMAKE_VISIBILITY_INLINES_HIDDEN 1)

project(stufflib_prj)

include(GenerateExportHeader)

find_package(TIFF REQUIRED CONFIG)

add_subdirectory(src)
