import gemtext

if __name__ == '__main__':
    file = open('example.gmi')
    text = file.read()

    parser_ = gemtext.parser.Parser()
    ast_ = parser_.parse(text)

    #print(ast_)

    #renderer_ = gemtext.renderer.HTMLRenderer()
    #html = renderer_.render(ast_)

    #print(html)

    renderer_ = gemtext.renderer.MarkdownRenderer()
    md = renderer_.render(ast_)
    print(md)

