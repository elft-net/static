class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        html = ""
        if self.props is not None:
            for prop, value in self.props.items():
                html += f' {prop}="{value}"'
        return html
   
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        html = ""
        if self.tag is not None:
            html += f"<{self.tag}"
            if self.props is not None:
                for prop, value in self.props.items():
                    html += f" {prop}='{value}'"
            html += ">"
        if self.value is not None:
            html += self.value
        if self.tag is not None:
            html += f"</{self.tag}>"
        return html

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("A parent node should have have a tag")
        elif self.children is None:
            raise ValueError("A parent node must have children")

        html = ""
        for child in self.children:
            html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}r, {self.props})"

    
