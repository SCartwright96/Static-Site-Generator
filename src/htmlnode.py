from textnode import *

class HTMLNode():
    def __init__(self,tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props == None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self,tag, value, props = None):
        super().__init__(tag,value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Invalid HTML: no value")
        
        if self.tag == None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag Undefined")
        if self.children == None:
            raise ValueError("Missing Children")
        
        output_str = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            output_str+=child.to_html()
        output_str += f"</{self.tag}>"
        return output_str

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            new_node = LeafNode(None, text_node.text)
        case TextType.BOLD:
            new_node = LeafNode("b",text_node.text)
        case TextType.ITALIC:
            new_node = LeafNode("i",text_node.text)
        case TextType.CODE:
            new_node = LeafNode("code",text_node.text)
        case TextType.LINK:
            new_node = LeafNode("a",text_node.text,{"href": text_node.url})
        case TextType.IMAGE:
            new_node = LeafNode("img","",{"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError("Invalid TextType")
    return new_node