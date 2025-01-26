import unittest
from markdown_to_blocks import markdown_to_blocks

class Test_markdown_to_blocks(unittest.TestCase):
    def test__markdown_to_blocks__with_empty_string__returns_empty_list(self):
        result = markdown_to_blocks("")

        self.assertEqual(result, [])

    def test__markdown_to_blocks__with_single_line___returns_single_block(self):
        markdown = """test line"""
        expected_blocks = [markdown]

        actual_blocks = markdown_to_blocks(markdown)

        self.assertEqual(actual_blocks, expected_blocks)

    def test__markdown_to_blocks__with_single_line_with_newlines_and_spaces_on_both_sides___returns_single_block(self):
        markdown = """
   
test line   
   

"""
        expected_blocks = ["test line"]

        actual_blocks = markdown_to_blocks(markdown)

        self.assertEqual(actual_blocks, expected_blocks)

    def test__markdown_to_blocks__with_multiple_line_block_with_newlines_and_spaces_on_both_sides___returns_single_block(self):
        markdown = """
   
test line
another line
some more lines   
   

"""
        expected_blocks = ["test line\nanother line\nsome more lines"]

        actual_blocks = markdown_to_blocks(markdown)

        self.assertEqual(actual_blocks, expected_blocks)

    def test__markdown_to_blocks__with_multiple_blocks___returns_expected_block(self):
        markdown = """
   
   test line
another line
some more lines   
   

 another block
with lines
  
 

"""
        expected_blocks = ["test line\nanother line\nsome more lines", "another block\nwith lines"]

        actual_blocks = markdown_to_blocks(markdown)

        self.assertEqual(actual_blocks, expected_blocks)
