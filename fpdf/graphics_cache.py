class GraphicsCache:
    """Graphics Cache

    basic cache for use with graphics code
    """

    INITIALIZATION_DATA = {
        "style_to_name": {},
        "name_to_style": {},
    }

    def __init__(self, data=None):
        super().__init__()
        self.data = {} if data is None else data
        self.data.update(self.INITIALIZATION_DATA)

    def lookup_style_from_name(self, name):
        return self.data["name_to_style"].get(name)

    def lookup_name_from_style(self, style):
        return self.data["style_to_name"].get(style)

    def count_saved_styles(self):
        return len(self.data["style_to_name"])

    def new_style_with_name(self, style, name):
        self.data["style_to_name"][style] = name
        self.data["name_to_style"][name] = style
