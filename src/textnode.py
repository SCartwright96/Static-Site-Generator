from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    TEXT = "text"

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, node2):
        return (repr(self) == repr(node2))

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def split_nodes_delimiter(old_nodes, delimiter, new_type):
    output_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            output_nodes.append(node)
            continue
        new_strings = node.text.split(delimiter)
        if len(new_strings)%2==0:
            raise ValueError("Invallid Markdown Syntax")
        if len(new_strings)==1:
            cur_nodes = [node]
        else:
            cur_nodes = []
            for i in range(len(new_strings)):
                if new_strings[i] == "":
                    continue
                if i%2 ==0:
                    cur_nodes.append(TextNode(new_strings[i],TextType.TEXT))
                else:
                    cur_nodes.append(TextNode(new_strings[i],new_type))

        output_nodes.extend(cur_nodes)

    return output_nodes
    