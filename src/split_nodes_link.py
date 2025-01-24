from ctypes import Array
from typing import Tuple
from extract_markdown_links import extract_markdown_links
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


def split_nodes_link(old_nodes: list):
    def split_node_link(old_node: TextNode, link_delimiter: Tuple[str, str]):
        text, url = link_delimiter
        new_nodes = []
        #new_nodes.append(TextNode(f"DEBUG: ({text}, {url})", TextType.BOLD))
        delimiter = f"[{text}]({url})"
        split_texts = old_node.text.split(delimiter)
        if len(split_texts) <= 1:
            return [old_node]
        #print(split_texts)
        is_first = True
        for split_text in split_texts:
            if not is_first:
                new_node = TextNode(text, TextType.LINK, url)
                #print(new_node)
                new_nodes.append(new_node)
            if len(split_text) > 0:
                new_node = TextNode(split_text, node.text_type, node.url)
                #print(new_node)
                new_nodes.append(new_node)
            is_first = False
        return new_nodes

    def split_node_links(old_node):
        link_delimiters = extract_markdown_links(old_node.text)
        if len(link_delimiters) == 0:
            if len(old_node.text) > 0:
                return [old_node]
            return []
       
        new_nodes = [old_node]
        for delimiter in link_delimiters:
            temp_nodes = list(new_nodes)
            for node in temp_nodes:
                index = new_nodes.index(node)
                new_nodes[index:index+1] = split_node_link(node, delimiter)
        return new_nodes

    new_nodes = []
    node: TextNode
    for node in old_nodes:
        if (node.text_type == TextType.LINK or node.text_type == TextType.LINK):
            new_nodes.append(node)
            continue
        new_nodes.extend(split_node_links(node))
    return new_nodes

# nodes = split_nodes_link([
#     TextNode("a [test-text](test-url) b", TextType.TEXT)
#     , TextNode("[test-text](test-url) b", TextType.TEXT)
#     , TextNode("a [test-text](test-url)", TextType.TEXT)
#     , TextNode("[test-text](test-url)", TextType.TEXT)
#     , TextNode("a [test-text](test-url) b [test2-text](test2-url) c", TextType.TEXT)
#     , TextNode("a b", TextType.TEXT)
#     , TextNode("", TextType.TEXT)
#     , TextNode("test [test-text](test-url) text [test2-text](test2-url)[test3-text](test3-url) word [test4-text](test4-url) best", TextType.TEXT)
# ])
# print("\n-- Result --")
# node: TextNode
# for node in nodes:
#     if not node.text.startswith("DEBUG"):
#         print(node)
