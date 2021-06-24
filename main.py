#!/usr/bin/python3
# Requires svglib and cairosvg to be installed
import subprocess
import argparse
from . import IconBuilder
from svglib.svglib import svg2rlg
import cairosvg


import os
import io

path_to_svg_file = "svg/base_odoo_icon_text.svg"
string_to_search = "{module}"
path_to_updated_svg = "svg/icon.svg"
path_to_exported_png = "svg/icon.png"
path_to_dev_icon_svg = "svg/accomodata_develop_icon.svg"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='This nifty program makes a new icon for your project',
    )
    parser.add_argument(
        '-t',
        '--type',
        default='dev',
        dest='type',
        help='''This is the type of icon. Default is [dev], for a dev icon'''
    )
    parser.add_argument(
        '-m',
        '--model',
        default='model',
        dest='model',
        help='''set the name of the model.'''
    )
    args = parser.parse_args()

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

    replacer(args.model)
