import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        self.test_tag = "P"
        self.test_value = "test text"
        self.test_props = { "href": "http://example.com", "class": "hover-show" }


    def test__leafnode__when_created_with_no_props__all_properties_have_expected_values(self):
        node = LeafNode(self.test_tag, self.test_value)

        self.assertEqual(node.tag, self.test_tag)
        self.assertEqual(node.value, self.test_value)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test__leafnode__when_created_with_all_parameters__all_properties_have_expected_values(self):
        node = LeafNode(self.test_tag, self.test_value, self.test_props)

        self.assertEqual(node.tag, self.test_tag)
        self.assertEqual(node.value, self.test_value)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, self.test_props)

    def test__leafnode__when_converted_to_string__results_in_expected_string(self):
        expected_string = "Tag: P, Value: test text, Children: None, Props: {'href': 'http://example.com', 'class': 'hover-show'}"
        node = LeafNode(self.test_tag, self.test_value, self.test_props)

        string = str(node)

        self.assertEqual(string, expected_string)

    def test__props_to_html__when_called__returns_expected_attributes_string(self):
        node = LeafNode(self.test_tag, self.test_value, self.test_props)

        attributes_string = node.props_to_html()

        self.assertEqual(attributes_string, " href=\"http://example.com\" class=\"hover-show\"")

    def test__props_to_html__with_no_props__returns_empty_string(self):
        node = LeafNode(self.test_tag, self.test_value)

        attributes_string = node.props_to_html()

        self.assertEqual(attributes_string, "")

    def test__to_html__with_no_value__raises_value_error(self):
        node = LeafNode(self.test_tag, None, self.test_props)

        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()