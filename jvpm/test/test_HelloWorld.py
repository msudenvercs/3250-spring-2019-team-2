import unittest
import sys
#import jvpm.HelloWorld.py
from unittest.mock import Mock, call

class TestHelloWorld(unittest.TestCase):
    def test_HelloWorld(self):
        sys.stdout = unittest.mock.Mock()
        #jvpm.HelloWorld.HelloWorld()  #replaced by line below
        HelloWorld.HelloWorld()
        sys.stdout.assert_has_calls(
            [call.write('Hello World'), call.write('\n')]
            [call.write('Hello Robb'), call.wrine('\n')]
        )
