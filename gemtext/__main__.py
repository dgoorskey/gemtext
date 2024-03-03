from . import parser
from . import renderer

import sys

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('Usage: gemtext [OPTIONS] [GEMTEXT_FILES]')
        sys.exit(0)

    paths = sys.argv[1:]

    for path in paths:
        file = open(path)
        text = file.read()

        parser_ = parser.Parser()
        ast_ = parser_.parse(text)

        renderer_ = renderer.MarkdownRenderer()
        md = renderer_.render(ast_)

        print(md)
