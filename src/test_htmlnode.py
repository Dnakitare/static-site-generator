import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
  def test_init(self):
    node = HTMLNode(tag="div", value="Hello, World!", children=[], props={"class": "container"})
    self.assertEqual(node.tag, "div")
    self.assertEqual(node.value, "Hello, World!")
    self.assertEqual(node.children, [])
    self.assertEqual(node.props, {"class": "container"})

  # def test_to_html(self):
  #   node = HTMLNode(tag="div", value="Hello, World!", children=[], props={"class": "container"})
  #   html = node.to_html()
  #   self.assertEqual(html, '<div class="container">Hello, World!</div>')

  def test_props_to_html(self):
    node = HTMLNode(tag="div", value="Hello, World!", children=[], props={"class": "container", "id": "my-div"})
    props_html = node.props_to_html()
    self.assertEqual(props_html, ' class="container" id="my-div"')

  def test_repr(self):
    node = HTMLNode(tag="div", value="Hello, World!", children=[], props={"class": "container"})
    node_repr = repr(node)
    self.assertEqual(node_repr, 'HTMLNode(div, Hello, World!, [], {"class": "container"})')

class TestLeafNode(unittest.TestCase):
  def test_init(self):
    node = LeafNode(value="Hello, World!", tag="div", props={"class": "container"})
    self.assertEqual(node.tag, "div")
    self.assertEqual(node.value, "Hello, World!")
    self.assertEqual(node.children, None)
    self.assertEqual(node.props, {"class": "container"})

  def test_to_html(self):
    node = LeafNode(value="Hello, World!", tag="div", props={"class": "container"})
    html = node.to_html()
    self.assertEqual(html, '<div class="container">Hello, World!</div>')

  def test_repr(self):
    node = LeafNode(value="Hello, World!", tag="div", props={"class": "container"})
    node_repr = repr(node)
    self.assertEqual(node_repr, 'HTMLNode(div, Hello, World!, None, {"class": "container"})')

if __name__ == '__main__':
  unittest.main()
