import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        paranode = HTMLNode("p", "Boot.dev")
        anchornode = HTMLNode("a", "Visit Boot.dev", [paranode], {"href": "https://www.boot.dev", "target":"_blank"})

        self.assertEqual(anchornode.props_to_html(), 
                         "href=https://www.boot.dev target=_blank")
        
        


if __name__ == "__main__":
    unittest.main()