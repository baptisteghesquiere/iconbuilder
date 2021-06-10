# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Requires svglib and cairosvg to be installed

from svglib.svglib import svg2rlg
import cairosvg


import os
import io

path_to_svg_file = "svg/base_odoo_icon_text.svg"
string_to_search = "{modulet}"
path_to_updated_svg = "svg/icon.svg"
path_to_png = "svg/icon.png"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    name = input("Geef de naam van de module:")

    def replacer(name):
        f = open(path_to_svg_file,'r')
        data = f.read()
        data = data.replace(string_to_search, name)
        f.close()
        f = open(path_to_updated_svg, "wt")
        f.write(data)
        f.close()
        cairosvg.svg2png(path_to_updated_svg, write_to=path_to_png)
        print(f)
        print(str(name))

    replacer(name)
