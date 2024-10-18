cmake_minimum_required(VERSION 3.26)

project(stufflibtestpkg_prj)

include(CTest)

find_package(stuff REQUIRED CONFIG)

add_executable(stufflibtestpkg)
target_sources(stufflibtestpkg PRIVATE stufflibtestpkg.cpp)
target_link_libraries(stufflibtestpkg PRIVATE stuff::stuff)
add_test(
    NAME stufflibtestpkg
    COMMAND $<TARGET_FILE:stufflibtestpkg>
)
