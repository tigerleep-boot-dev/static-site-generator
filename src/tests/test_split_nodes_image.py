import unittest
from split_nodes_image import split_nodes_image
from textnode import TextNode, TextType

class Test_split_nodes_image(unittest.TestCase):
    def test__split_nodes_image__with_no_nodes__returns_empty_list(self):
        text_nodes = []

        nodes = split_nodes_image(text_nodes)

        self.assertEqual(nodes, [])

    def test_split_nodes_image__with_no_images__returns_same_nodes(self):
        text_nodes = [TextNode("test text", TextType.TEXT)]

        nodes = split_nodes_image(text_nodes)

        self.assertEqual(nodes, text_nodes)

    def test_split_nodes_image__with_image_in_middle__returns_expected_nodes(self):
        text_nodes = [TextNode("test ![test-text](test-url) text", TextType.TEXT)]
        expected_nodes = [TextNode("test ", TextType.TEXT), TextNode("test-text", TextType.IMAGE, "test-url"), TextNode(" text", TextType.TEXT)]

        nodes = split_nodes_image(text_nodes)

        self.assertEqual(nodes, expected_nodes)

    def test_split_nodes_image__with_image_in_beginning__returns_expected_nodes(self):
        text_nodes = [TextNode("![test-text](test-url) text", TextType.TEXT)]
        expected_nodes = [TextNode("test-text", TextType.IMAGE, "test-url"), TextNode(" text", TextType.TEXT)]

        nodes = split_nodes_image(text_nodes)

        self.assertEqual(nodes, expected_nodes)

    def test_split_nodes_image__with_image_in_end__returns_expected_nodes(self):
        text_nodes = [TextNode("test ![test-text](test-url)", TextType.TEXT)]
        expected_nodes = [TextNode("test ", TextType.TEXT), TextNode("test-text", TextType.IMAGE, "test-url")]

        nodes = split_nodes_image(text_nodes)

        self.assertEqual(nodes, expected_nodes)

    def test_split_nodes_image__with_image_only__returns_expected_nodes(self):
        text_nodes = [TextNode("![test-text](test-url)", TextType.TEXT)]
        expected_nodes = [TextNode("test-text", TextType.IMAGE, "test-url")]

        nodes = split_nodes_image(text_nodes)

        self.assertEqual(nodes, expected_nodes)

    def test_split_nodes_image__with_multiple_images__returns_expected_nodes(self):
        text_nodes = [TextNode("test ![test-text](test-url) text ![test2-text](test2-url)![test3-text](test3-url) word ![test4-text](test4-url) best", TextType.TEXT)]
        expected_nodes = [
            TextNode("test ", TextType.TEXT)
            , TextNode("test-text", TextType.IMAGE, "test-url")
            , TextNode(" text ", TextType.TEXT)
            , TextNode("test2-text", TextType.IMAGE, "test2-url")
            , TextNode("test3-text", TextType.IMAGE, "test3-url")
            , TextNode(" word ", TextType.TEXT)
            , TextNode("test4-text", TextType.IMAGE, "test4-url")
            , TextNode(" best", TextType.TEXT)
        ]

        nodes = split_nodes_image(text_nodes)

        self.assertEqual(nodes, expected_nodes)
