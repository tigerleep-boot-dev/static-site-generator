import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        self.test_tag = "A"
        self.test_children = [
            LeafNode("B", "text 1", { "class": "red" })
            , ParentNode("I", [LeafNode("DIV", "text 2", { "class": "green" }), LeafNode("SPAN", "text 3", { "class": "blue" })],{ "data-rock": "yes" }
        )]
        self.test_props = { "href": "http://example.com", "class": "hover-show" }
        self.test_html = "<A href=\"http://example.com\" class=\"hover-show\"><B class=\"red\">text 1</B><I data-rock=\"yes\"><DIV class=\"green\">text 2</DIV><SPAN class=\"blue\">text 3</SPAN></I></A>"
        self.test_string = "Tag: A, Value: None, Children: [Tag: B, Value: text 1, Children: None, Props: {'class': 'red'}, Tag: I, Value: None, Children: [Tag: DIV, Value: text 2, Children: None, Props: {'class': 'green'}, Tag: SPAN, Value: text 3, Children: None, Props: {'class': 'blue'}], Props: {'data-rock': 'yes'}], Props: {'href': 'http://example.com', 'class': 'hover-show'}"


    def test__parentnode__when_created_with_no_props__all_properties_have_expected_values(self):
        node = ParentNode(self.test_tag, self.test_children)

        self.assertEqual(node.tag, self.test_tag)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, self.test_children)
        self.assertEqual(node.props, None)

    def test__parentnode__when_created_with_all_parameters__all_properties_have_expected_values(self):
        node = ParentNode(self.test_tag, self.test_children, self.test_props)

        self.assertEqual(node.tag, self.test_tag)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, self.test_children)
        self.assertEqual(node.props, self.test_props)

    def test__parentnode__when_converted_to_string__results_in_expected_string(self):

        node = ParentNode(self.test_tag, self.test_children, self.test_props)

        string = str(node)

        self.assertEqual(string, self.test_string)

    def test__props_to_html__when_called__returns_expected_attributes_string(self):
        node = ParentNode(self.test_tag, self.test_children, self.test_props)

        attributes_string = node.props_to_html()

        self.assertEqual(attributes_string, " href=\"http://example.com\" class=\"hover-show\"")

    def test__props_to_html__with_no_props__returns_empty_string(self):
        node = ParentNode(self.test_tag, self.test_children)

        attributes_string = node.props_to_html()

        self.assertEqual(attributes_string, "")

    def test__to_html__with_no_tag__raises_value_error(self):
        node = ParentNode(None, self.test_children, self.test_props)

        with self.assertRaises(ValueError):
            node.to_html()

    def test__to_html__with_no_children__raises_value_error(self):
        node = ParentNode(self.test_tag, None, self.test_props)

        with self.assertRaises(ValueError):
            node.to_html()

    def test__to_html__with_valid_properties__results_in_expected_html(self):
        node = ParentNode(self.test_tag, self.test_children, self.test_props)

        html = node.to_html()

        self.assertEqual(html, self.test_html)

    def test__to_html__with_empty_children__results_in_expected_html(self):
        node = ParentNode(self.test_tag, [], self.test_props)

        html = node.to_html()

        self.assertEqual(html, "<A href=\"http://example.com\" class=\"hover-show\"></A>")

if __name__ == "__main__":
    unittest.main()