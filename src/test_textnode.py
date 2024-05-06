import unittest
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        text_node = TextNode("Hello World", "text")
        text_node2 = TextNode("Hello World", "text")
        self.assertEqual(text_node, text_node2)

if __name__ == "__main__":
    unittest.main()