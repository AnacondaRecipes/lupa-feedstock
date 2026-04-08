#!/usr/bin/env bash

# Unvendor bundled Lua/LuaJIT sources: delete vendored third-party code
rm -rf third-party

$PYTHON -m pip install . -vv --no-build-isolation --no-deps
