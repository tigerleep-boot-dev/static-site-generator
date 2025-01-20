import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        self.test_tag = "P"
        self.test_value = "test text"
        self.test_children = [HTMLNode("A", "link text", props={ "href": "http://example.com" }), HTMLNode("STRONG", "bold text")]
        self.test_props = { "href": "http://example.com", "class": "hover-show" }

    def test__htmlnode__when_created_with_no_parameters__all_properties_are_none(self):
        node = HTMLNode()

        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test__htmlnode__when_created_with_all_parameters__all_properties_have_expected_values(self):
        node = HTMLNode(self.test_tag, self.test_value, self.test_children, self.test_props)

        self.assertEqual(node.tag, self.test_tag)
        self.assertEqual(node.value, self.test_value)
        self.assertEqual(node.children, self.test_children)
        self.assertEqual(node.props, self.test_props)

    def test__htmlnode__when_converted_to_string__results_in_expected_string(self):
        expected_string = "Tag: P, Value: test text, Children: [Tag: A, Value: link text, Children: None Props: {'href': 'http://example.com'}, Tag: STRONG, Value: bold text, Children: None Props: None] Props: {'href': 'http://example.com', 'class': 'hover-show'}"
        node = HTMLNode(self.test_tag, self.test_value, self.test_children, self.test_props)

        string = str(node)

        self.assertEqual(string, expected_string)

    def test__props_to_html__when_called__returns_expected_attributes_string(self):
        node = HTMLNode(self.test_tag, self.test_value, self.test_children, self.test_props)

        attributes_string = node.props_to_html()

        self.assertEqual(attributes_string, " href=\"http://example.com\" class=\"hover-show\"")

    def test__props_to_html__with_no_props__returns_empty_string(self):
        node = HTMLNode(self.test_tag, self.test_value, self.test_children)

        attributes_string = node.props_to_html()

        self.assertEqual(attributes_string, "")


if __name__ == "__main__":
    unittest.main()