import subprocess

# requires inkscape to be installed
class IconBuilder:

    def __init__(self):
        self.path_to_templates = "svg/"
        self.string_to_search = ""
        self.updated_svg = ""
        self.exported_png = ""
        self.base_svg = ""

    def set_string_to_search(self, search_string):
        self.string_to_search = search_string
        return

    def get_string_to_search(self):
        return self.string_to_search

    def set_updated_svg(self, updated_svg):
        self.updated_svg = updated_svg
        return

    def get_updated_svg(self):
        return self.updated_svg

    def set_exported_png(self, exported_png):
        self.exported_png = exported_png
        return

    def get_exported_png(self):
        return self.exported_png

    def set_base_svg(self, base_svg):
        self.base_svg = base_svg
        return

    def get_base_svg(self):
        return self.base_svg

    def build_svg_path(self, svg):
        self.set_base_svg(svg)
        path = self.path_to_templates + self.get_base_svg()
        return path

    def replacer(self, string_to_search, new_string):
        ''' open the file '''