import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq_none(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_eq(self):
        node = HTMLNode(tag="p", value="text here")
        node2 = HTMLNode(tag="p", value="text here")
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode(tag="p", value="text here", props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')


if __name__ == "__main__":
    unittest.main()
