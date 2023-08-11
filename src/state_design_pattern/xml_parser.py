class Node:
    def __init__(self, tag_name, parent=None):
        self.parent = parent
        self.tag_name = tag_name
        self.children = []
        self.text = None

    def __str__(self) -> str:
        if self.text is not None:
            return self.tag_name + " " + self.text
        else:
            return self.tag_name


class TextNode:
    def process(self, remaining_string, parser):
        idx_start_tag = remaining_string.find("<")
        text = remaining_string[:idx_start_tag]
        parser.current_node.text = text
        parser.state = ChildNode()
        return remaining_string[idx_start_tag:]


class CloseTag:
    def process(self, remaining_string, parser):
        idx_start_tag = remaining_string.find("<")
        idx_end_tag = remaining_string.find(">")
        assert remaining_string[idx_start_tag + 1] == "/"
        tag_name = remaining_string[idx_start_tag + 2 : idx_end_tag]
        assert tag_name == parser.current_node.tag_name
        parser.current_node = parser.current_node.parent
        parser.state = ChildNode()
        return remaining_string[idx_end_tag + 1 :].strip()


class OpenTag:
    def process(self, remaining_string, parser):
        idx_start_tag = remaining_string.find("<")
        idx_end_tag = remaining_string.find(">")
        tag_name = remaining_string[idx_start_tag + 1 : idx_end_tag]

        node = Node(tag_name, parent=parser.current_node)
        parser.current_node.children.append(node)
        parser.current_node = node
        parser.state = ChildNode()
        return remaining_string[idx_end_tag + 1 :].strip()


class ChildNode:
    def process(self, remaining_string, parser):
        stripped = remaining_string.strip()
        if stripped.startswith("</"):
            parser.state = CloseTag()
        elif stripped.startswith("<"):
            parser.state = OpenTag()
        else:
            parser.state = TextNode()

        return stripped


class FirstTag:
    def process(self, remaining_string, parser):
        idx_start_tag = remaining_string.find("<")
        idx_end_tag = remaining_string.find(">")
        tag_name = remaining_string[idx_start_tag + 1 : idx_end_tag]

        root = Node(tag_name)
        parser.root = root
        parser.current_node = root
        parser.state = ChildNode()
        return remaining_string[idx_end_tag + 1 :]


class Parser:
    def __init__(self, parse_string):
        self.parse_string = parse_string
        self.root = None
        self.current_state = None
        self.state = FirstTag()

    def process(self, remaining_string):
        remaining = self.state.process(remaining_string, self)
        if remaining:
            self.process(remaining)

    def start(self):
        self.process(self.parse_string)


if __name__ == "__main__":
    import os

    input_file = os.path.join(os.path.dirname(__file__), "input_file.xml")

    with open(input_file) as infile:
        input_text = "".join(infile.readlines())
        input_text = input_text.replace(os.linesep, "")

    parser = Parser(input_text)
    parser.start()

    # print the parser content

    nodes = [parser.root]
    while nodes:
        node = nodes.pop(0)
        print(node)
        nodes = node.children + nodes
