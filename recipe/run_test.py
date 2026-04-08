import unittest

import lupa


class TestLupaSmoke(unittest.TestCase):
    def test_import_and_version(self):
        self.assertTrue(hasattr(lupa, "__version__"))
        self.assertEqual(lupa.__version__, "2.6")

    def test_runtime_creation(self):
        lua = lupa.LuaRuntime()
        self.assertIsNotNone(lua)
        self.assertTrue(lua.lua_implementation.startswith(("Lua", "LuaJIT")))

    def test_eval(self):
        lua = lupa.LuaRuntime()
        self.assertEqual(lua.eval("1+1"), 2)
        self.assertEqual(lua.eval("...", 1, 2, 3), (1, 2, 3))

    def test_execute(self):
        lua = lupa.LuaRuntime()
        self.assertEqual(lua.execute("return 2 + 3"), 5)

    def test_lua_version(self):
        lua = lupa.LuaRuntime()
        version = lua.lua_version
        self.assertIsInstance(version, tuple)
        self.assertGreaterEqual(version, (5, 1))
        self.assertLess(version[0], 6)
        self.assertEqual(version, lupa.LUA_VERSION)

    def test_table(self):
        lua = lupa.LuaRuntime()
        table = lua.table(1, 2, 3, a=10)
        self.assertEqual(len(table), 3)
        self.assertEqual(table[1], 1)
        self.assertEqual(table[2], 2)
        self.assertEqual(table[3], 3)
        self.assertEqual(table["a"], 10)

    def test_table_from(self):
        lua = lupa.LuaRuntime()
        table = lua.table_from({"foo": 1, "bar": 2}, recursive=True)
        self.assertEqual(table["foo"], 1)
        self.assertEqual(table["bar"], 2)

    def test_python_callback(self):
        lua = lupa.LuaRuntime()

        def add_one(x):
            return x + 1

        func = lua.eval("function(f, x) return f(x) end")
        self.assertEqual(func(add_one, 4), 5)

    def test_require_string(self):
        lua = lupa.LuaRuntime()
        stringlib = lua.require("string")
        self.assertEqual(stringlib.lower("ABC"), "abc")

    def test_none_roundtrip(self):
        lua = lupa.LuaRuntime()
        func = lua.eval("function() return python.none end")
        self.assertIsNone(func())


if __name__ == "__main__":
    unittest.main(verbosity=2)
