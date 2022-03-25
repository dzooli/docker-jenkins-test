import pytest


class Test001BasicSuite:

    def test_true(self):
        assert True

    def test_false(self):
        a = False
        assert a == False
