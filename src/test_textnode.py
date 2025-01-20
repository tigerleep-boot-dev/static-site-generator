import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test__textnode__when_created_with_url__has_expected_property_values(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://example.com")

        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.text_type, TextType.BOLD)
        self.assertEqual(node.url, "http://example.com")

    def test__textnode__when_created_without_url__has_expected_property_values(self):
        node = TextNode("This is a text node", TextType.BOLD)

        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.text_type, TextType.BOLD)
        self.assertEqual(node.url, None)

    def test__eq__with_equal_textnodes__returns_true(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)

        self.assertEqual(node, node2)

    def test__eq__with_textnodes_differing_only_by_text__returns_false(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://example.com")
        node2 = TextNode("This is a different text node", TextType.BOLD, "http://example.com")

        self.assertNotEqual(node, node2)

    def test__eq__with_textnodes_differing_only_by_text_type__returns_false(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://example.com")
        node2 = TextNode("This is a text node", TextType.ITALIC, "http://example.com")

        self.assertNotEqual(node, node2)

    def test__eq__with_textnodes_differing_only_by_url__returns_false(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://www.example.com")

        self.assertNotEqual(node, node2)

    def test__textnode_with_all_three_properties__when_converted_to_string__results_in_expected_string(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://example.com")
        expected_string = "TextNode(This is a text node Bold http://example.com)"

        string = str(node)

        self.assertEqual(string, expected_string)

    def test__textnode_without_url__when_converted_to_string__results_in_expected_string(self):
        node = TextNode("This is a text node", TextType.BOLD)
        expected_string = "TextNode(This is a text node Bold None)"

        string = str(node)

        self.assertEqual(string, expected_string)

if __name__ == "__main__":
    unittest.main()