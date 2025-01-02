import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node = TextNode("This is a text node", TextType.BOLD, "Web.site")
        node2 = TextNode("This is a text node", TextType.BOLD, "Web.site")
        self.assertEqual(node, node2)

        node = TextNode("This is a text node", TextType.BOLD, "Web.site")
        node2 = TextNode("This is a text node", TextType.BOLD, "Web.sites")
        self.assertNotEqual(node, node2)

        node = TextNode("This is a text node", TextType.ITALIC, "Web.site")
        node2 = TextNode("This is a text node", TextType.BOLD, "Web.site")
        self.assertNotEqual(node, node2)

        node = TextNode("This is a texts node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()