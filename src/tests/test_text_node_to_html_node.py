import unittest
from text_node_to_html_node import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import HTMLNode

class Test_text_node_to_html_node(unittest.TestCase):
    def test__text_node_to_html_node__with_invalid_text_type__raises_value_exception(self):
        with self.assertRaises(ValueError):
            text_node_to_html_node(TextNode("test", "invalid-type", "url"))

    def test__text_node_to_html_node__with_text_node__returns_text_element(self):
        text_node = TextNode("test-text", TextType.TEXT, "test-url")

        html_node = text_node_to_html_node(text_node)

        self.assertEqual(html_node.to_html(), "test-text")

    def test__text_node_to_html_node__with_bold_node__returns_b_element(self):
        text_node = TextNode("test-text", TextType.BOLD, "test-url")

        html_node = text_node_to_html_node(text_node)

        self.assertEqual(html_node.to_html(), "<b>test-text</b>")

    def test__text_node_to_html_node__with_italic_node__returns_i_element(self):
        text_node = TextNode("test-text", TextType.ITALIC, "test-url")

        html_node = text_node_to_html_node(text_node)

        self.assertEqual(html_node.to_html(), "<i>test-text</i>")

    def test__text_node_to_html_node__with_code_node__returns_code_element(self):
        text_node = TextNode("test-text", TextType.CODE, "test-url")

        html_node = text_node_to_html_node(text_node)

        self.assertEqual(html_node.to_html(), "<code>test-text</code>")

    def test__text_node_to_html_node__with_link_node__returns_a_element(self):
        text_node = TextNode("test-text", TextType.LINK, "test-url")

        html_node = text_node_to_html_node(text_node)

        self.assertEqual(html_node.to_html(), "<a href=\"test-url\">test-text</a>")

    def test__text_node_to_html_node__with_image_node__returns_img_element(self):
        text_node = TextNode("test-text", TextType.IMAGE, "test-url")

        html_node = text_node_to_html_node(text_node)

        self.assertEqual(html_node.to_html(), "<img src=\"test-url\" alt=\"test-text\"></img>")
