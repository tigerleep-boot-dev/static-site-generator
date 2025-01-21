import unittest
from extract_markdown_links import extract_markdown_links

class Test_extract_markdown_links(unittest.TestCase):
    def test__extract_markdown_links__with_no_links__returns_empty_list(self):
        links = extract_markdown_links("there are no links")

        self.assertEqual(links, [])

    def test__extract_markdown_links__with_link__returns_text_and_url(self):
        links = extract_markdown_links("there [text](url) are links")

        self.assertEqual(links, [("text", "url")])

    def test__extract_markdown_links__with_multiple_links__returns_expected_number_of_links(self):
        links = extract_markdown_links("there [text](url) are [text2](url2) links")

        self.assertEqual(len(links), 2)

    def test__extract_markdown_links__with_multiple_links__returns_expected_links(self):
        links = extract_markdown_links("there [text](url) are [text2](url2) links")

        self.assertEqual(links, [("text", "url"), ("text2", "url2")])

    def test__extract_markdown_links__with_open_parenthesis_in_link_text__returns_text_and_url(self):
        links = extract_markdown_links("there [te(xt](url) are links")

        self.assertEqual(links, [("te(xt", "url")])
