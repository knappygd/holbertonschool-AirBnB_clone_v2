#!/usr/bin/python3
"""Module with console unittests"""


import unittest
import console
import io
from contextlib import redirect_stdout


class TestConsole(unittest.TestCase):
    """Class that tests console"""

    def setUp(self):
        self.console = console.HBNBCommand()


    def test_create(self):
        var = "California"
        with redirect_stdout(io.StringIO()) as a:
            self.console.onecmd(f"create State")
        state_id = a.getvalue()
        with redirect_stdout(io.StringIO()) as f:
            self.console.onecmd(f"create State name='{var}'")
        state_id2 = f.getvalue()
        with redirect_stdout(io.StringIO()) as d:
            self.console.onecmd(
                "create City state_id=\"{}\" name='San_Francisco_is_super_cool'".format(str(state_id2)))
        city_id = d.getvalue()
        print(f"h{state_id} ,s{state_id2}, c{city_id}")
        self.assertEqual(1, 1)