import re

def markdown_to_blocks(markdown):
    split_pattern = r"(\s*\n\s*){2,}"
    blocks = re.split(split_pattern, markdown)
    new_blocks = []
    for block in blocks:
        if not re.match("^\s*$", block):
            new_blocks.append(block)
    return new_blocks

# markdown = r"""# This is a heading

# This is a paragraph of text. It has some **bold** and *italic* words inside of it.

# * This is the first list item in a list block
# * This is a list item
# * This is another list item"""
# print(markdown_to_blocks(markdown))
