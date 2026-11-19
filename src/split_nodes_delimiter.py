from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_list = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_list.append(old_node)

        else:
            if old_node.text.count(delimiter) % 2 != 0:
                raise Exception("invalid Markdwn syntax")
            new_nodes = old_node.text.split(delimiter)

            i = 1

            for new_node in new_nodes:
                if new_node == "":
                    i += 1
                    continue
                if i % 2 == 0:
                    new_list.append(TextNode(new_node, text_type))
                else:
                    new_list.append(TextNode(new_node, TextType.TEXT))
                i += 1

    return new_list
