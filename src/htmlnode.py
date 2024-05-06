class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError()
  
  def props_to_html(self):
    html = ''
    for k,v in self.props.items():
      html += F' {k}="{v}"'
    return html
  
  def __repr__(self):
    props = ', '.join([f'"{k}": "{v}"' for k, v in self.props.items()])
    return F'HTMLNode({self.tag}, {self.value}, {self.children}, {{{props}}})'
  
class LeafNode(HTMLNode):
  def __init__(self, value, tag=None, props=None):
    super().__init__(tag, value, None, props)

  def to_html(self):
    return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'