# pygobject-stubs-generator

# NOTE: THIS IS UNFINISHED AND REQUIRES MANUAL WORK!

This parses `.gir` files in `/usr/share/gir-1.0` and creates `.pyi` files for any found GIR file. This does not handle union parameters, tuple parameters and return values, and numerous other features. It may also not have proper formatting. This should be used to create a base `pyi` file that should be used to easily modify the generated stubs for [PyGObject-Stubs](https://github.com/pygobject/pygobject-stubs).
