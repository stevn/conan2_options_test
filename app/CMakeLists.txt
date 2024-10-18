cmake_minimum_required(VERSION 3.26)

project(stufftool_prj)

include(CTest)

find_package(stuff REQUIRED CONFIG)
find_package(opencv REQUIRED CONFIG)

add_subdirectory(src)
