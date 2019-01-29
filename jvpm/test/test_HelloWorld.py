import unittest
import sys
import jvpm.HelloWorld
from unittest.mock import Mock, call

class TestHelloWorld(unittest.TestCase):
    def test_HelloWorld(self):
        sys.stdout = unittest.mock.Mock()
        jvpm.HelloWorld.HelloWorld()
        sys.stdout.assert_has_calls(
            [call.write('Hello World'), call.write('\n'),
			call.write('Hello Robb'), call.write('\n'),
			call.write('Hello Justin'), call.write('\n'),
            call.write('Hello Megan'), call.write('\n')]

        )
