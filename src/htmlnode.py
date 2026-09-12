class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag:str | None = tag
        self.value:str | None = value
        self.children:list | None = children
        self.props:dict | None = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html:str = ""

        if self.props != None and self.props != {}:
            for prop in self.props:
                html = html + " " + f'{prop}="{self.props[prop]}"'
        return html

    def __eq__(self, value: "HTMLNode") -> bool:
        return self.tag == value.tag and self.value == value.value and self.children == value.children and self.props == value.props

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
