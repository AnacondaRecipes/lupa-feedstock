# Unvendor bundled Lua/LuaJIT sources: delete vendored third-party code
if exist third-party rd /s /q third-party

REM On Windows, build Lupa against the external conda-provided LuaJIT instead of
REM vendored sources or pkg-config discovery. setup.py supports explicit paths
REM via --lua-lib / --lua-includes, so we pass the import library and headers
REM directly and invoke setup.py to ensure these custom options are recognized.
%PYTHON% setup.py --lua-lib "%LIBRARY_LIB%\lua51.lib" --lua-includes "%LIBRARY_INC%\luajit-2.1" build_ext install
if errorlevel 1 exit 1
