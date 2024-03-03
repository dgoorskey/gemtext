"""
# This is a heading
This is the first paragraph.
* a list item
* another list item
This is the second paragraph.
=> http://example.org/ Absolute URI
=> //example.org/ No scheme URI
=> /robots.txt Just a path URI
=> GemText a page link
"""

class DocumentItem:
    def __init__(self):
        return

class Document:
    def __init__(self, items: list[DocumentItem] = []) -> None:
        self.items: list[DocumentItem] = list(items)
    
    def add_item(self, item: DocumentItem) -> None:
        self.items.append(item)
    
    def __str__(self) -> str:
        return 'Document(' + ', '.join(str(item) for item in self.items) + ')'

class BlankLine(DocumentItem):
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return 'BlankLine()'

class Heading(DocumentItem):
    def __init__(self, level: int, text: str) -> None:
        assert(level >= 1 and level <= 3)
        self.level = level
        self.text = text
    
    def __str__(self) -> str:
        return 'Heading(' + str(self.level) + ', "' + self.text + '")'

class Paragraph(DocumentItem):
    def __init__(self, text: str) -> None:
        self.text = text
    
    def __str__(self) -> str:
        return 'Paragraph("' + self.text + '")'

class ListItem:
    def __init__(self, text: str) -> None:
        self.text = text
    
    def __str__(self) -> str:
        return 'ListItem("' + self.text + '")'

class List(DocumentItem):
    def __init__(self, items: list[ListItem] = []) -> None:
        self.items = list(items)
    
    def add_item(self, item: ListItem) -> None:
        self.items.append(item)
    
    def __str__(self) -> str:
        return 'List(' + ', '.join(str(item) for item in self.items) + ')'

class Link(DocumentItem):
    def __init__(self, url: str, text: str = '') -> None:
        self.url = url
        self.text = text
    
    def __str__(self) -> str:
        return 'Link("' + self.url + '", "' + self.text + '")'

class BlockQuote(DocumentItem):
    def __init__(self, text: str = '') -> None:
        self.text = text
    
    def __str__(self) -> str:
        return 'BlockQuote("' + self.text + '")'

class Pre(DocumentItem):
    def __init__(self, alttext: str = '', text: str = '') -> None:
        self.alttext = alttext
        self.text = text
    
    def add_text(self, text: str) -> None:
        self.text += text
    
    def __str__(self) -> str:
        return 'Pre("' + self.alttext + '", "' + self.text + '")'
