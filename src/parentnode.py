from src.htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError
        if self.children == None:
            raise ValueError

        total = ""

        for child in self.children:
            total = total + child.to_html()
        return f'<{self.tag}>{total}</{self.tag}>'
