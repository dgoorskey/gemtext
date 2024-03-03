from . import ast
from . import parser
from . import renderer

if __name__ == '__main__':
    file = open('example.gmi')
    gemtext = file.read()

    parser_ = parser.Parser()
    ast_ = parser_.parse(gemtext)

    # print(ast_)

    renderer_ = renderer.HTMLRenderer()
    html = renderer_.render(ast_)

    print(html)

