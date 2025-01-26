import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

space_textnode = TextNode(" ", TextType.TEXT)
class Test_text_to_textnodes(unittest.TestCase):
    def test__text_to_textnodes__with_empty_text__returns_empty_list(self):
        text = ""

        nodes = text_to_textnodes(text)

        self.assertEqual(nodes, [])

    def test_text_to_textnodes__with_markdown__returns_one_node_with_entire_text(self):
        text = "abc"
        expected_nodes = [TextNode(text, TextType.TEXT)]

        nodes = text_to_textnodes(text)

        self.assertEqual(nodes, expected_nodes)

    def test_text_to_textnodes__with_bold_text__returns_expected_nodes(self):
        text = "abc **md-text** def"
        expected_nodes = [TextNode("abc ", TextType.TEXT), TextNode("md-text", TextType.BOLD), TextNode(" def", TextType.TEXT)]

        nodes = text_to_textnodes(text)

        self.assertEqual(nodes, expected_nodes)

    def test_text_to_textnodes__with_italic_text__returns_expected_nodes(self):
        text = "abc *md-text* def"
        expected_nodes = [TextNode("abc ", TextType.TEXT), TextNode("md-text", TextType.ITALIC), TextNode(" def", TextType.TEXT)]

        nodes = text_to_textnodes(text)

        self.assertEqual(nodes, expected_nodes)

    def test_text_to_textnodes__with_bold_text_before_italic_text__returns_expected_nodes(self):
        text = "abc **md-text** *md2-text* def"
        expected_nodes = [TextNode("abc ", TextType.TEXT), TextNode("md-text", TextType.BOLD), space_textnode, TextNode("md2-text", TextType.ITALIC), TextNode(" def", TextType.TEXT)]

        nodes = text_to_textnodes(text)

        self.assertEqual(nodes, expected_nodes)

    def test_text_to_textnodes__with_italic_text_before_bold_text__returns_expected_nodes(self):
        text = "abc *md-text* **md2-text** def"
        expected_nodes = [TextNode("abc ", TextType.TEXT), TextNode("md-text", TextType.ITALIC), space_textnode, TextNode("md2-text", TextType.BOLD), TextNode(" def", TextType.TEXT)]

        nodes = text_to_textnodes(text)

        self.assertEqual(nodes, expected_nodes)

    def test_text_to_textnodes__with_code_text__returns_expected_nodes(self):
        text = "abc `md-text` def"
        expected_nodes = [TextNode("abc ", TextType.TEXT), TextNode("md-text", TextType.CODE), TextNode(" def", TextType.TEXT)]

        nodes = text_to_textnodes(text)

        self.assertEqual(nodes, expected_nodes)

    def test_text_to_textnodes__with_image__returns_expected_nodes(self):
        text = "abc ![md-text](md-url) def"
        expected_nodes = [TextNode("abc ", TextType.TEXT), TextNode("md-text", TextType.IMAGE, "md-url"), TextNode(" def", TextType.TEXT)]

        nodes = text_to_textnodes(text)

        self.assertEqual(nodes, expected_nodes)

    def test_text_to_textnodes__with_link__returns_expected_nodes(self):
        text = "abc [md-text](md-url) def"
        expected_nodes = [TextNode("abc ", TextType.TEXT), TextNode("md-text", TextType.LINK, "md-url"), TextNode(" def", TextType.TEXT)]

        nodes = text_to_textnodes(text)

        self.assertEqual(nodes, expected_nodes)

    def test_text_to_textnodes__with_image_before_link__returns_expected_nodes(self):
        text = "abc ![md-text](md-url) [md2-text](md2-url) def"
        expected_nodes = [TextNode("abc ", TextType.TEXT), TextNode("md-text", TextType.IMAGE, "md-url"), space_textnode, TextNode("md2-text", TextType.LINK, "md2-url"), TextNode(" def", TextType.TEXT)]

        nodes = text_to_textnodes(text)

        self.assertEqual(nodes, expected_nodes)

    def test_text_to_textnodes__with_link_before_image__returns_expected_nodes(self):
        text = "abc [md-text](md-url) ![md2-text](md2-url) def"
        expected_nodes = [TextNode("abc ", TextType.TEXT), TextNode("md-text", TextType.LINK, "md-url"), space_textnode, TextNode("md2-text", TextType.IMAGE, "md2-url"), TextNode(" def", TextType.TEXT)]

        nodes = text_to_textnodes(text)

        self.assertEqual(nodes, expected_nodes)

    def test_text_to_textnodes__with_multiple_markdown_types__returns_expected_nodes(self):
        text = "abc **bold** *italic* _italic2_ `code` ![image](image-url) [link](link-url) def"
        expected_nodes = [
            TextNode("abc ", TextType.TEXT)
            , TextNode("bold", TextType.BOLD), space_textnode
            , TextNode("italic", TextType.ITALIC), space_textnode
            , TextNode("italic2", TextType.ITALIC), space_textnode
            , TextNode("code", TextType.CODE), space_textnode
            , TextNode("image", TextType.IMAGE, "image-url"), space_textnode
            , TextNode("link", TextType.LINK, "link-url")
            , TextNode(" def", TextType.TEXT)
        ]

        nodes = text_to_textnodes(text)

        self.assertEqual(nodes, expected_nodes)

    #     nodes = text_to_textnodes(text)

    #     self.assertEqual(nodes, expected_nodes)
