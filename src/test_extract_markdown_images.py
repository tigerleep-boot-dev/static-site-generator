import unittest
from extract_markdown_images import extract_markdown_images
from textnode import TextNode, TextType
from htmlnode import HTMLNode

class Test_extract_markdown_images(unittest.TestCase):
    def test__extract_markdown_images__with_no_images__returns_empty_list(self):
        images = extract_markdown_images("there are no images")

        self.assertEqual(images, [])

    def test__extract_markdown_images__with_image__returns_text_and_url(self):
        images = extract_markdown_images("there ![text](url) are images")

        self.assertEqual(images, [("text", "url")])

    def test__extract_markdown_images__with_multiple_images__returns_expected_number_of_images(self):
        images = extract_markdown_images("there ![text](url) are ![text2](url2) images")

        self.assertEqual(len(images), 2)

    def test__extract_markdown_images__with_open_parenthesis_in_image_text__returns_text_and_url(self):
        images = extract_markdown_images("there ![te(xt](url) are images")

        self.assertEqual(images, [("te(xt", "url")])
