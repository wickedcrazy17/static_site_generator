import unittest
from extract_markdown_links import extract_markdown_links

class TestExtractMarkdownImages(unittest.TestCase):
    def test_eq(self):
        node = ("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        node1 = extract_markdown_links(node)
        node2 = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node = ("")
        node1 = extract_markdown_links(node)
        node2 = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertNotEqual(node1, node2)

    def test_eq_none(self):
        node1 = extract_markdown_links("")
        node2 = []
        self.assertEqual(node1, node2)

    def test_extract_markdown_images(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)

if __name__ == "__main__":
    unittest.main()
