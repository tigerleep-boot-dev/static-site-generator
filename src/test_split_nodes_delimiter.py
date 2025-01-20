import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class Test_split_nodes_delimiter(unittest.TestCase):
    def test__split_nodes_delimiter__with_no_nodes__returns_empty_list(self):
        text_nodes = []

        nodes = split_nodes_delimiter(text_nodes, "*", TextType.BOLD)

        self.assertEqual(nodes, [])

    def test_split_nodes_delimiter__with_no_delimited_text__returns_expected_nodes(self):
        text_nodes = [TextNode("test text", TextType.TEXT)]
        expected_nodes = [TextNode("test text", TextType.TEXT)]

        nodes = split_nodes_delimiter(text_nodes, "*", TextType.BOLD)

        self.assertEqual(nodes, expected_nodes)

    def test_split_nodes_delimiter__with_delimited_text_in_middle__returns_expected_nodes(self):
        text_nodes = [TextNode("test *bold* text", TextType.TEXT)]
        expected_nodes = [TextNode("test ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" text", TextType.TEXT)]

        nodes = split_nodes_delimiter(text_nodes, "*", TextType.BOLD)

        self.assertEqual(nodes, expected_nodes)

    def test_split_nodes_delimiter__with_delimited_text_in_beginning__returns_expected_nodes(self):
        text_nodes = [TextNode("*bold* text", TextType.TEXT)]
        expected_nodes = [TextNode("bold", TextType.BOLD), TextNode(" text", TextType.TEXT)]

        nodes = split_nodes_delimiter(text_nodes, "*", TextType.BOLD)

        self.assertEqual(nodes, expected_nodes)

    def test_split_nodes_delimiter__with_delimited_text_in_end__returns_expected_nodes(self):
        text_nodes = [TextNode("test *bold*", TextType.TEXT)]
        expected_nodes = [TextNode("test ", TextType.TEXT), TextNode("bold", TextType.BOLD)]

        nodes = split_nodes_delimiter(text_nodes, "*", TextType.BOLD)

        self.assertEqual(nodes, expected_nodes)

    def test_split_nodes_delimiter__with_delimited_text_onlt__returns_expected_nodes(self):
        text_nodes = [TextNode("*bold*", TextType.TEXT)]
        expected_nodes = [TextNode("bold", TextType.BOLD)]

        nodes = split_nodes_delimiter(text_nodes, "*", TextType.BOLD)

        self.assertEqual(nodes, expected_nodes)

    def test_split_nodes_delimiter__with_multiple_delimited_text__returns_expected_nodes(self):
        text_nodes = [TextNode("test *bold* text *also **included* word *and* best", TextType.TEXT)]
        expected_nodes = [
            TextNode("test ", TextType.TEXT)
            , TextNode("bold", TextType.BOLD)
            , TextNode(" text ", TextType.TEXT)
            , TextNode("also ", TextType.BOLD)
            , TextNode("included", TextType.BOLD)
            , TextNode(" word ", TextType.TEXT)
            , TextNode("and", TextType.BOLD)
            , TextNode(" best", TextType.TEXT)
        ]

        nodes = split_nodes_delimiter(text_nodes, "*", TextType.BOLD)

        self.assertEqual(nodes, expected_nodes)

    def test_split_nodes_delimiter__with_multiple_delimiters__returns_expected_nodes(self):
        text_nodes = [TextNode("test *bold* text **also **`included` word", TextType.TEXT)]
        expected_nodes = [
            TextNode("test ", TextType.TEXT)
            , TextNode("bold", TextType.BOLD)
            , TextNode(" text ", TextType.TEXT)
            , TextNode("also ", TextType.ITALIC)
            , TextNode("included", TextType.CODE)
            , TextNode(" word", TextType.TEXT)
        ]

        nodes = split_nodes_delimiter(text_nodes, "**", TextType.ITALIC)
        nodes = split_nodes_delimiter(nodes, "*", TextType.BOLD)
        nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

        self.assertEqual(nodes, expected_nodes)
