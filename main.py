#!usr/bin/env python3
# Requires svglib and cairosvg to be installed
import subprocess

from svglib.svglib import svg2rlg
import cairosvg


import os
import io

path_to_svg_file = "svg/base_odoo_icon_text.svg"
string_to_search = "{module}"
path_to_updated_svg = "svg/icon.svg"
path_to_exported_png = "svg/icon.png"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    name = input("Geef de naam van de module:")

    def replacer(name):
        f = open(path_to_svg_file, "rt")
        data = f.read()
        data = data.replace(string_to_search, name)
        f.close()
        f = open(path_to_updated_svg, "wt")
        f.write(data)
        f.close()
        subprocess.run(['inkscape', path_to_updated_svg, '-e', path_to_exported_png])
        print(f)
        print(str(name))

    replacer(name)
