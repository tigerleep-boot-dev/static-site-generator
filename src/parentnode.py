from functools import reduce
from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("tag must not be None")
        if self.children == None:
            raise ValueError("children must not be None")
        inner_html = reduce(
            lambda html, node: f"{html}{node.to_html()}"
            , self.children
            , ""
        )
        return f"<{self.tag}{self.props_to_html()}>{inner_html}</{self.tag}>"
