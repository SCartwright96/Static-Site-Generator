from htmlnode import *
from textnode import *
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
        test_node = LeafNode("a","Actions",{"Test": "Test2"})
        self.assertEqual(test_node.to_html(), """<a Test="Test2">Actions</a>""")

    def test_leaf_no_tag(self):
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

    def test_TextNode_to_HTML(self):
        print("text node to HTML test: ")
        test_text_node = TextNode("This is bold", TextType.BOLD)
        test_leaf_node = text_node_to_html_node(test_text_node)
        expected_leaf_node = LeafNode("b", "This is bold")
        print(test_leaf_node)
        self.assertEqual(repr(test_leaf_node), repr(expected_leaf_node))

    def test_TextNode_to_HTML_Link(self):
        print("text node to HTML test: ")
        test_text_node = TextNode("This is a link", TextType.LINK, "test.com")
        test_leaf_node = text_node_to_html_node(test_text_node)
        expected_leaf_node = LeafNode("a", "This is a link", {"href": "test.com"})
        print(test_leaf_node)
        self.assertEqual(repr(test_leaf_node), repr(expected_leaf_node))

    def test_TextNode_to_HTML_Image(self):
        print("text node to HTML test: ")
        test_text_node = TextNode("This is alt text", TextType.IMAGE, "test.com")
        test_leaf_node = text_node_to_html_node(test_text_node)
        expected_leaf_node = LeafNode("img", "", {"src": "test.com", "alt": "This is alt text"})
        print(test_leaf_node)
        self.assertEqual(repr(test_leaf_node), repr(expected_leaf_node))

if __name__ == "__main__":
    unittest.main()