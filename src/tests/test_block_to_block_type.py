import unittest

from block_to_block_type import block_to_block_type

class Test_block_to_block_type(unittest.TestCase):
    def test__block_to_block_type__with_empty_string__returns_normal(self):
        block = ""
        expected_type = "NORMAL"

        type = block_to_block_type(block)

        self.assertEqual(type, expected_type)

    def test__block_to_block_type__with_normal_string__returns_normal(self):
        block = "Mary had a little"
        expected_type = "NORMAL"

        type = block_to_block_type(block)

        self.assertEqual(type, expected_type)

    def test__block_to_block_type__with_heading_level_one__returns_h1(self):
        block = "# Mary had a little"
        expected_type = "H1"

        type = block_to_block_type(block)

        self.assertEqual(type, expected_type)

    def test__block_to_block_type__with_heading_level_three__returns_h1(self):
        block = "### Mary had a little"
        expected_type = "H3"

        type = block_to_block_type(block)

        self.assertEqual(type, expected_type)

    def test__block_to_block_type__with_heading_level_six__returns_h1(self):
        block = "###### Mary had a little"
        expected_type = "H6"

        type = block_to_block_type(block)

        self.assertEqual(type, expected_type)

    def test__block_to_block_type__with_heading_level_seven__returns_normal(self):
        block = "####### Mary had a little"
        expected_type = "NORMAL"

        type = block_to_block_type(block)

        self.assertEqual(type, expected_type)

    def test__block_to_block_type__with_code__returns_code(self):
        block = "```Mary had a little```"
        expected_type = "CODE"

        type = block_to_block_type(block)

        self.assertEqual(type, expected_type)

    def test__block_to_block_type__only_starting_with_code__returns_normal(self):
        block = "```Mary had a little"
        expected_type = "NORMAL"

        type = block_to_block_type(block)

        self.assertEqual(type, expected_type)

    def test__block_to_block_type__only_ending_with_code__returns_normal(self):
        block = "Mary had a little```"
        expected_type = "NORMAL"

        type = block_to_block_type(block)

        self.assertEqual(type, expected_type)

    def test__block_to_block_type__with_one_unordered_list_line_using_asterisk__returns_ulist(self):
        block = "* Mary had a little"
        expected_type = "ULIST"

        type = block_to_block_type(block)

        self.assertEqual(type, expected_type)

    def test__block_to_block_type__with_one_unordered_list_line_using_dash__returns_ulist(self):
        block = "- Mary had a little"
        expected_type = "ULIST"

        type = block_to_block_type(block)

        self.assertEqual(type, expected_type)

    def test__block_to_block_type__with_multiple_unordered_list_lines_using_dash_and_asterisk__returns_ulist(self):
        block = "- Mary\n- had\n* a\n- little"
        expected_type = "ULIST"

        type = block_to_block_type(block)

        self.assertEqual(type, expected_type)

    def test__block_to_block_type__with_multiple_unordered_list_lines_with_one_normal_line_in_middle__returns_normal(self):
        block = "- Mary\n- had\n a\n- little"
        expected_type = "NORMAL"

        type = block_to_block_type(block)

        self.assertEqual(type, expected_type)

    def test__block_to_block_type__with_one_ordered_list_line_using_0__returns_olist(self):
        block = "1. Mary had a little"
        expected_type = "OLIST"

        type = block_to_block_type(block)

        self.assertEqual(type, expected_type)

    def test__block_to_block_type__with_one_ordered_list_line_using_9__returns_olist(self):
        block = "9. Mary had a little"
        expected_type = "OLIST"

        type = block_to_block_type(block)

        self.assertEqual(type, expected_type)

    def test__block_to_block_type__with_multiple_ordered_list_lines__returns_olist(self):
        block = "1. Mary\n3. had\n4. a\n8. little"
        expected_type = "OLIST"

        type = block_to_block_type(block)

        self.assertEqual(type, expected_type)

    def test__block_to_block_type__with_multiple_ordered_list_lines_with_one_normal_line_in_middle__returns_normal(self):
        block = "1. Mary\n3. had\na\n8. little"
        expected_type = "NORMAL"

        type = block_to_block_type(block)

        self.assertEqual(type, expected_type)
