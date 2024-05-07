from textnode import (
  TextNode,
  text_type_text,
  text_type_bold,
  text_type_italic,
  text_type_code,
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        # Directly add non-matching nodes to the new list
        if old_node.text_type != text_type:
            new_nodes.append(old_node)
            continue
        
        sections = old_node.text.split(delimiter)
        # Check for an even number of sections, which indicates unclosed markdown
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        
        # Iterate through sections and assign the appropriate text type
        for i, section in enumerate(sections):
            if section:  # Skip empty sections
                node_type = text_type if i % 2 != 0 else text_type_text
                new_nodes.append(TextNode(section, node_type))
    return new_nodes