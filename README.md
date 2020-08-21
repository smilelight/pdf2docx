# pdf2docx 

[dothinking/pdf2docx](https://github.com/dothinking/pdf2docx)魔改版本

## 改动列表

- 原有PyMuPDF有错误识别blocks的情况，这里将blocks中的每一个line都视为一个block
- 将word写入时的tab_stop调整为first_text_indent（便于libreoffice将其转换为html后得到样式特征）
- 增加判断段落（都是一行）是否居中的判断，如果居中，则将段落对齐情况设置为居中（原来都是左对齐）

## Features

- [x] Parse and re-create text format
	- [x] font style, e.g. font name, size, weight, italic and color
    - [x] highlight, underline, strike-through converted from docx
    - [x] highlight, underline, strike-through applied from PDF annotations
- [ ] Parse and re-create list style
- [x] Parse and re-create table
    - [x] border style, e.g. width, color
    - [x] shading style, i.e. background color
    - [x] merged cells
    - [x] vertical direction cell
- [x] Rebuild page layout in docx
	- [x] text in horizontal direction: from left to right
	- [x] text in vertical direction: from bottom to top
	- [x] in-line image
    - [x] paragraph layout: horizontal and vertical spacing

*It can also be used as a tool to extract table contents since both table content and format/style is parsed.*

## Limitations

- Text-based PDF file only
- Normal reading direction only
    - horizontal/vertical paragraph/line/word
    - no word transformation, e.g. rotation
- No floating images
- Full borders table only


## Installation

```bash
pip install -U git+https://github.com/smilelight/pdf2docx.git@master
```

## Usage

### By range of pages

```
$ pdf2docx test.pdf test.docx --start=5 --end=10
```

### By page numbers

```
$ pdf2docx test.pdf test.docx --pages=5,7,9
```

```
$ pdf2docx --help

NAME
    pdf2docx - Run the pdf2docx parser.

SYNOPSIS
    pdf2docx PDF_FILE DOCX_FILE <flags>

DESCRIPTION
    Run the pdf2docx parser.

POSITIONAL ARGUMENTS
    PDF_FILE
        PDF filename to read from
    DOCX_FILE
        DOCX filename to write to

FLAGS
    --start=START
        first page to process, starting from zero
    --end=END
        last page to process, starting from zero
    --pages=PAGES
        range of pages
    --debug=DEBUG
        create illustration pdf showing layouts if True, else do nothing

NOTES
    You can also use flags syntax for POSITIONAL ARGUMENTS
```

### As a library

```python
''' With this library installed with 
    `pip install pdf2docx`, or `python setup.py install`.
'''

from pdf2docx.main import parse

pdf_file = '/path/to/sample.pdf'
docx_file = 'path/to/sample.docx'

# convert pdf to docx
parse(pdf_file, docx_file, start=0, end=1)
```

Or just to extract tables,

```python
from pdf2docx.main import extract_tables

pdf_file = '/path/to/sample.pdf'

tables = extract_tables(pdf_file, start=0, end=1)
for table in tables:
    print(table)

# outputs
...
[['Input ', None, None, None, None, None], 
['Description A ', 'mm ', '30.34 ', '35.30 ', '19.30 ', '80.21 '],
['Description B ', '1.00 ', '5.95 ', '6.16 ', '16.48 ', '48.81 '],
['Description C ', '1.00 ', '0.98 ', '0.94 ', '1.03 ', '0.32 '],
['Description D ', 'kg ', '0.84 ', '0.53 ', '0.52 ', '0.33 '],
['Description E ', '1.00 ', '0.15 ', None, None, None],
['Description F ', '1.00 ', '0.86 ', '0.37 ', '0.78 ', '0.01 ']]
```

## Sample

![sample_compare.png](https://s1.ax1x.com/2020/08/04/aDryx1.png)