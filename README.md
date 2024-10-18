# conan2_options_test

Conan options handling is flawed:

- Hard-coded package options may be overridden silently without the user noticing that something bad is happening under the hood.
- Conflicting options should lead to an error instead of silently being modified.

## Introduction

In this reproduction scenario a library package `stuff/1.0.0` is required by an application package `stufftool/1.0.0`.

There is a (transitive) dependency on `libtiff`:

- The `stuff` library package requires libtiff directly.
- The `stufftool` application package requires `opencv`, which in turn requires `libtiff`.
- The application doesn't really know / care that `opencv` and `stuff` each have `libtiff` as dependency. It is agnostic to that transitive dependency, since it doesn't use libtiff itself.

In this example, let's assume that we want to disable the `jbig` option of `libtiff`. The JBIG package is very problematic for closed-source software because it is licensed under GPL.

Therefore the `stuff` library makes sure to disable the `jbig` option by hard-coding the option to `False` in the `configure()` function of its `conanfile.py` recipe.

## Build + Reproduce

On Unix-like operating systems run:

    ./create_all.sh

This currently produces this error:

    CMake Error: Could not create named generator DummyGeneratorToPreventBuildingOfJBIG

Here the build of `jbig` has been made to fail on purpose by setting a non-existent CMake generator name `DummyGeneratorToPreventBuildingOfJBIG` for `jbig` in `global.conf`.
This shall stop the build process as soon as Conan attempts to automatically build JBIG, because we do not want that.

## Error summary

When building `stufftool`, its `opencv` dependency defaults to `libtiff` with **`jbig=True`** option. This leads to its `stuff` dependency silently becoming "corrupted" in a certain way.

Even though it configures a really important option, the **hard-coded option value `jbig=False` is ignored** and the `stuff` library is rebuilt with `jbig=True`! The stuff library with JBIG enabled should never exist, as it is explicitly disabled in its recipe.

Conan apparently automatically tries to "make things work" by only setting the options of a package once and then ignoring the later configure() calls. That seems problematic.

## Expected behavior

I would have expected Conan to **throw an error message** stating that a **package options conflict** has been found in the dependency tree.
