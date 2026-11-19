import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        node1 = split_nodes_delimiter([node], "**", TextType.BOLD)
        node2 = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT),
        ]
        self.assertEqual(node1, node2)

    def test_eq_2(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node1 = split_nodes_delimiter([node], "`", TextType.CODE)
        node2 = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node1 = split_nodes_delimiter([node], "`", TextType.CODE)
        node2 = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()
