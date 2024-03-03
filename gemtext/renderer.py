from . import ast

class HTMLRenderer:
    def __init__(self) -> None:
        pass
    
    def _render_blankline(self, blankline: ast.BlankLine) -> str:
        return '<br>\n'

    def _render_heading(self, heading: ast.Heading) -> str:
        return '<h' + str(heading.level) + '>' + heading.text + '</h' + str(heading.level) + '>\n'
    
    def _render_paragraph(self, paragraph: ast.Paragraph) -> str:
        return '<p>' + paragraph.text + '</p>\n'
    
    def _render_link(self, link: ast.Link) -> str:
        return '<a href="' + link.url + '">' + link.text + '</a>\n'
    
    def _render_list(self, list_: ast.List) -> str:
        result = '<ul>\n'

        for item in list_.items:
            result += '<li>' + item.text + '</li>\n'

        result += '</ul>\n'
        return result
    
    def _render_blockquote(self, blockquote: ast.BlockQuote) -> str:
        return '<blockquote>' + blockquote.text + '</blockquote>\n'
    
    def _render_pre(self, pre: ast.Pre) -> str:
        sanitized = pre.text.replace('<', '&lt;').replace('>', '&gt;')
        return '<pre>' + sanitized + '</pre>\n'

    def render(self, document: ast.Document) -> str:
        html = ''

        for item in document.items:
            if isinstance(item, ast.BlankLine):
                html += self._render_blankline(item)
            elif isinstance(item, ast.Heading):
                html += self._render_heading(item)
            elif isinstance(item, ast.Paragraph):
                html += self._render_paragraph(item)
            elif isinstance(item, ast.Link):
                html += self._render_link(item)
            elif isinstance(item, ast.List):
                html += self._render_list(item)
            elif isinstance(item, ast.BlockQuote):
                html += self._render_blockquote(item)
            elif isinstance(item, ast.Pre):
                html += self._render_pre(item)

        return html

class MarkdownRenderer:
    def __init__(self) -> None:
        pass

    def _render_blankline(self, blankline: ast.BlankLine) -> str:
        return '\n\n'

    def _render_heading(self, heading: ast.Heading) -> str:
        return ('#' * heading.level) + ' ' + heading.text + '\n\n'
    
    def _render_paragraph(self, paragraph: ast.Paragraph) -> str:
        return paragraph.text + '\n\n'
    
    def _render_link(self, link: ast.Link) -> str:
        return '[' + link.text + '](' + link.url + ')\n\n'
    
    def _render_list(self, list_: ast.List) -> str:
        result = ''
        for item in list_.items:
            result += '- ' + item.text + '\n'
        result += '\n\n'
        return result
    
    def _render_blockquote(self, blockquote: ast.BlockQuote) -> str:
        return '> ' + blockquote.text + '\n\n'
    
    def _render_pre(self, pre: ast.Pre) -> str:
        return '```' + pre.alttext + '\n' + pre.text + '```\n\n'

    def render(self, document: ast.Document) -> str:
        md = ''

        for item in document.items:
            if isinstance(item, ast.BlankLine):
                md += self._render_blankline(item)
            elif isinstance(item, ast.Heading):
                md += self._render_heading(item)
            elif isinstance(item, ast.Paragraph):
                md += self._render_paragraph(item)
            elif isinstance(item, ast.Link):
                md += self._render_link(item)
            elif isinstance(item, ast.List):
                md += self._render_list(item)
            elif isinstance(item, ast.BlockQuote):
                md += self._render_blockquote(item)
            elif isinstance(item, ast.Pre):
                md += self._render_pre(item)

        return md

