class HTMLNode: 
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        return f'href={self.props['href']} target={self.props['target']}'
    
    def __repr__(self):
        print('Object:', self)
        print('Tag:', self.tag)
        print('Children:', self.children)
        print('Props:', self.props)


