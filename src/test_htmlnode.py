import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
  def test_init(self):
    node = HTMLNode(tag="div", value="Hello, World!", children=[], props={"class": "container"})
    self.assertEqual(node.tag, "div")
    self.assertEqual(node.value, "Hello, World!")
    self.assertEqual(node.children, [])
    self.assertEqual(node.props, {"class": "container"})

  def test_to_html(self):
    node = HTMLNode(tag="div", value="Hello, World!", children=[], props={"class": "container"})
    with self.assertRaises(NotImplementedError):
      node.to_html()

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

class TestParentNode(unittest.TestCase):
  def test_init(self):
    node = ParentNode(children=[], tag="div", props={"class": "container"})
    self.assertEqual(node.tag, "div")
    self.assertEqual(node.value, None)
    self.assertEqual(node.children, [])
    self.assertEqual(node.props, {"class": "container"})

  def test_to_html(self):
    node = ParentNode(children=[LeafNode(value="Hello, World!", tag="p", props={"class": "paragraph"})], tag="div", props={"class": "container"})
    html = node.to_html()
    self.assertEqual(html, '<div class="container"><p class="paragraph">Hello, World!</p></div>')

  def test_repr(self):
    node = ParentNode(children=[], tag="div", props={"class": "container"})
    node_repr = repr(node)
    self.assertEqual(node_repr, 'HTMLNode(div, None, [], {"class": "container"})')

  def test_to_html_no_tag(self):
    node = ParentNode(children=[], props={"class": "container"})
    with self.assertRaises(ValueError):
      node.to_html()

  def test_to_html_no_children(self):
    node = ParentNode(None, tag="div", props={"class": "container"})
    with self.assertRaises(ValueError):
      node.to_html()


    

if __name__ == '__main__':
  unittest.main()
