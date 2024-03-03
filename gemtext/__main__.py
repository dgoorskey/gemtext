from . import parser
from . import renderer

import sys

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('Usage: gemtext [OPTIONS] [GEMTEXT_FILES]')
        sys.exit(0)

    options: list[str] = []
    idxarg = 1
    for arg in sys.argv[1:]:
        if arg == '--':
            idxarg += 1
            break
        if not arg.startswith('--'):
            break
        options.append(arg)
        idxarg += 1
    
    target = 0
    for option in options:
        if option == '--html':
            target = 0
        elif option == '--markdown':
            target = 1
        else:
            print('gemtext: unrecognized option "' + option + '"')

    paths = sys.argv[idxarg:]

    for path in paths:
        file = open(path)
        text = file.read()

        parser_ = parser.Parser()
        ast_ = parser_.parse(text)

        result = ''
        if target == 0:
            renderer_ = renderer.HTMLRenderer()
            result = renderer_.render(ast_)
        elif target == 1:
            renderer_ = renderer.MarkdownRenderer()
            result = renderer_.render(ast_)
        print(result)

