from htmlnode import *
import unittest

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        test_node = HTMLNode("TestTag","TestValue","TestChildren","TestProps")
        print("Expected: TestTag=TestValue TestChildren=TestProps")
        print(f"Actual: {repr(test_node)}")
        self.assertEqual(repr(test_node), "HTMLNode(TestTag, TestValue, TestChildren, TestProps)")

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
        self.assertEqual(repr(test_node), "HTMLNode(TestTag, None, TestChildren, TestProps)")

    def test_leaf(self):
        print("Leaf Test")
        test_node = LeafNode("a","Actions",{"Test": "Test2"})
        self.assertEqual(test_node.to_html(), """<a Test="Test2">Actions</a>""")

    def test_leaf_no_tag(self):
        print("Leaf Test")
        test_node = LeafNode(None,"Actions",{"Test": "Test2"})
        self.assertEqual(test_node.to_html(), "Actions")

    def test_leaf_repr(self):
        test_node = LeafNode("a","Actions","")
        self.assertEqual(repr(test_node), "HTMLNode(a, Actions, None, )")

    def test_ParentNode(self):
        test_leaf = LeafNode("a","Actions","")
        middle_parent = ParentNode("Mid",{test_leaf})
        top_parent = ParentNode("Top",{middle_parent})
        self.assertEqual(top_parent.to_html(),"<Top><Mid><a>Actions</a></Mid></Top>")

    def test_ParentNodeProps(self):
        test_leaf = LeafNode("a","Actions","")
        middle_parent = ParentNode("Mid",[test_leaf],{"MidTag": "MidTest"})
        top_parent = ParentNode("Top",[middle_parent], {"TopTag": "TopTest", "Top2":"TopTest2"})
        self.assertEqual(top_parent.to_html(),"""<Top TopTag="TopTest" Top2="TopTest2"><Mid MidTag="MidTest"><a>Actions</a></Mid></Top>""")

if __name__ == "__main__":
    unittest.main()