from functools import reduce

class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props == None:
            return ""
        return reduce(
            lambda attributes, prop: f"{attributes} {prop[0]}=\"{prop[1]}\""
            , self.props.items()
            , ""
        )

    def __repr__(self):
        return f"Tag: {self.tag}, Value: {self.value}, Children: {self.children} Props: {self.props}"
