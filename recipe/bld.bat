# Unvendor bundled Lua/LuaJIT sources: delete vendored third-party code
if exist third-party rd /s /q third-party

REM On Windows, build Lupa against an external conda-provided Lua implementation
REM instead of vendored sources or pkg-config discovery. setup.py supports explicit
REM paths via --lua-lib / --lua-includes, so we pass the import library and headers
REM directly and invoke setup.py to ensure these custom options are recognized.
REM
REM LuaJIT has no official MSVC/ARM64 port (its ARM64 support relies on the
REM clang/GCC toolchains, not MSVC), so win-arm64 builds against plain Lua instead.
IF "%ARCH%"=="arm64" (
    %PYTHON% setup.py --lua-lib "%LIBRARY_LIB%\lua.lib" --lua-includes "%LIBRARY_INC%" build_ext install
) ELSE (
    %PYTHON% setup.py --lua-lib "%LIBRARY_LIB%\lua51.lib" --lua-includes "%LIBRARY_INC%\luajit-2.1" build_ext install
)
if errorlevel 1 exit 1
