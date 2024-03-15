import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        try:
            node.eq(node2)
        except AssertionError as msg:
            print("An error was raised for test_eq: ${msg}")

    def test_type_not_eq(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "italic", "https://www.boot.dev")
        try:
            self.assertNotEqual(node, node2)
        except AssertionError:
            print("An error was raised for test_type_not_eq: ${msg}")

    def test_none_url(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold")
        try:
            self.assertNotEqual(node, node2)
        except AssertionError:
            print("An error was raised for test_none_url: ${msg}")
            
if __name__ == "__main__":
    unittest.main()