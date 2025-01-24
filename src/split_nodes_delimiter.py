from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: TextType):
    new_nodes = []

    node: TextNode
    for node in old_nodes:
        if (node.text_type == TextType.IMAGE or node.text_type == TextType.LINK):
            new_nodes.append(node)
            continue
        split_text = node.text.split(delimiter)
        is_new_type = False
        for text in split_text:
            if not is_new_type:
                if len(text) > 0:
                    new_nodes.append(TextNode(text, node.text_type))
            else:
                if len(text) > 0:
                    new_nodes.append(TextNode(text, text_type))
            is_new_type = not is_new_type
    return new_nodes
