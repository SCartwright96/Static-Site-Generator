from htmlnode import *
import unittest

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        test_node = HTMLNode("TestTag","TestValue","TestChildren","TestProps")
        print("Expected: TestTag=TestValue TestChildren=TestProps")
        print(f"Actual: {repr(test_node)}")
        self.assertEqual(repr(test_node), " TestTag=TestValue TestChildren=TestProps")

    def test_tag(self):
        test_node = HTMLNode("TestTags","TestValue","TestChildren","TestProps")
        print("Expected: TestTag=TestValue TestChildren=TestProps")
        print(f"Actual: {repr(test_node)}")
        self.assertNotEqual(repr(test_node), " TestTag=TestValue TestChildren=TestProps")

    def test_value(self):
        test_node = HTMLNode("TestTag","TestValues","TestChildren","TestProps")
        print("Expected: TestTag=TestValue TestChildren=TestProps")
        print(f"Actual: {repr(test_node)}")
        self.assertNotEqual(repr(test_node), " TestTag=TestValue TestChildren=TestProps")

    def test_Child(self):
        test_node = HTMLNode("TestTag","TestValue","TestChildrens","TestProps")
        print("Expected: TestTag=TestValue TestChildren=TestProps")
        print(f"Actual: {repr(test_node)}")
        self.assertNotEqual(repr(test_node), " TestTag=TestValue TestChildren=TestProps")
    
    def test_prop(self):
        test_node = HTMLNode("TestTag","TestValue","TestChildren","TestProp")
        print("Expected: TestTag=TestValue TestChildren=TestProps")
        print(f"Actual: {repr(test_node)}")
        self.assertNotEqual(repr(test_node), " TestTag=TestValue TestChildren=TestProps")

    def test_missing(self):
        test_node = HTMLNode("TestTag",children="TestChildren",props="TestProps")
        print("Expected: TestTag=TestValue TestChildren=TestProps")
        print(f"Actual: {repr(test_node)}")
        self.assertEqual(repr(test_node), " TestTag=None TestChildren=TestProps")



if __name__ == "__main__":
    unittest.main()