from . import ast

class Parser:
    def __init__(self) -> None:
        self.lineno = 1

        self.in_list = False
        self.in_pre = False
        self.current_list: ast.Link = None
        self.current_pre: ast.Pre = None
        self.ast: ast.Document = None
    
    def _warn(self, message: str, lineno: int = None) -> None:
        if lineno is None:
            print('[WARNING] ' + message)
        else:
            print('[WARNING] line ' + str(lineno) + ': ' + message)
    
    def _try_parse_blankline(self, line: str) -> bool:
        if line != '': return False
        self.in_list = False
        
        node = ast.BlankLine()
        self.ast.add_item(node)

        return True

    def _try_parse_heading1(self, line: str) -> bool:        
        if line.startswith('#') and not line.startswith('# '):
            self._warn('This line looks like a heading, but is missing the mandatory space after the pound signs. It will be interpreted as a paragraph.', self.lineno)
            return False

        if not line.startswith('# '): return False
        self.in_list = False

        text = line[2:]
        node = ast.Heading(1, text)
        self.ast.add_item(node)

        return True

    def _try_parse_heading2(self, line: str) -> bool:
        if line.startswith('##') and not line.startswith('## '):
            self._warn('This line looks like a sub-heading, but is missing the mandatory space after the pound signs. It will be interpreted as a paragraph.', self.lineno)
            return False

        if not line.startswith('## '): return False
        self.in_list = False

        text = line[3:]
        node = ast.Heading(2, text)
        self.ast.add_item(node)

        return True

    def _try_parse_heading3(self, line: str) -> bool:
        if line.startswith('###') and not line.startswith('### '):
            self._warn('This line looks like a sub-sub-heading, but is missing the mandatory space after the pound signs. It will be interpreted as a paragraph.', self.lineno)
            return False

        if not line.startswith('### '): return False
        self.in_list = False

        text = line[4:]
        node = ast.Heading(3, text)
        self.ast.add_item(node)

        return True
    
    def _parse_paragraph(self, line: str) -> bool:
        self.in_list = False

        node = ast.Paragraph(line)
        self.ast.add_item(node)

        return True
    
    def _try_parse_link(self, line: str) -> bool:
        if not line.startswith('=>'): return False
        self.in_list = False

        tokens: list[str] = line[2:].lstrip().split()
        assert(len(tokens) >= 1)
        url = tokens[0]
        text = '' if len(tokens) < 2 else tokens[2]
        node = ast.Link(url, text)
        self.ast.add_item(node)

        return True
    
    def _try_parse_list(self, line: str) -> bool:
        if line.startswith('*') and not line.startswith('* '):
            self._warn('This looks like a list item, but is missing the mandatory space after the asterisk. It will be interpreted as a paragraph.', self.lineno)
            return False

        if not line.startswith('* '): return False

        # start a new list if we aren't currently in one
        if not self.in_list:
            l = ast.List()
            self.ast.add_item(l)
            self.current_list = l
        self.in_list = True

        text = line[2:]
        node = ast.ListItem(text)
        self.current_list.add_item(node)

        return True
    
    def _try_parse_blockquote(self, line: str) -> bool:
        if not line.startswith('>'): return False
        self.in_list = False

        text = line[1:].lstrip()
        node = ast.BlockQuote(text)
        self.ast.add_item(node)

        return True
    
    def _try_parse_pre(self, line: str) -> bool:
        if line.startswith('```') and self.in_pre:

            if line != '```':
                self._warn('This looks like the end of a preformatted section, but has text after the backticks. The text will be ignored.', self.lineno)

            self.in_pre = False
            return True
        
        if line.startswith('```') and not self.in_pre:
            self.in_pre = True
            alttext = line[3:]
            p = ast.Pre(alttext=alttext)
            self.ast.add_item(p)
            self.current_pre = p

            return True
        
        if not self.in_pre: return False

        self.current_pre.add_text(line + '\n') # BUG: doesn't preserve original line endings

        return True


    def _parse_line(self, line: str) -> None:
        if self._try_parse_pre(line):        return
        if not self.in_pre:
            if self._try_parse_blankline(line):  return
            if self._try_parse_heading3(line):   return
            if self._try_parse_heading2(line):   return
            if self._try_parse_heading1(line):   return
            if self._try_parse_link(line):       return
            if self._try_parse_list(line):       return
            if self._try_parse_blockquote(line): return
            self._parse_paragraph(line)
    
    def parse(self, gemtext: str) -> ast.Document:
        self.lineno = 1

        self.in_list = False
        self.in_pre = False
        self.current_list = None
        self.current_pre = None
        self.ast = ast.Document()

        for line in gemtext.splitlines():
            self._parse_line(line)
            self.lineno += 1
        
        return self.ast
