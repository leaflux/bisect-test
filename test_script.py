from script_1 import *

class TestErrors:
    def test_inc(self):
        assert inc(1) == 2

    def test_otherfunc(self):
        assert otherfunc(0, 0) == True

class TestMoreErrors:
    def test_complex_error(self):
        def f():
            return 44
        def g():
            return 45
        assert somefunc(f(), g()) == True
