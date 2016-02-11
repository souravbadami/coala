from queue import Queue

from bears.tests.LocalBearTestHelper import LocalBearTestHelper
from bears.python.PyUnusedCodeBear import PyUnusedCodeBear
from coalib.settings.Section import Section


class PyUnusedCodeBearTest(LocalBearTestHelper):

    def setUp(self):
        self.uut = PyUnusedCodeBear(Section('name'), Queue())

    def test_valid(self):
        self.assertLinesValid(self.uut, ["import sys; sys.do()"])
        self.assertLinesValid(self.uut, ["a = 2; print(a)"])

    def test_invalid(self):
        self.assertLinesValid(self.uut, ["import os"], valid=False)
        self.assertLinesValid(self.uut, ["pass"], valid=False)
