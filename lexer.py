

import re
import sys

KEYWORDS = {
    'int','char','bool','float','long','short','double','string',
    'signed','unsigned','break','case','class','const','continue',
    'default','delete','do','else','enum','false','for','friend',
    'if','namespace','new','private','protected','public','return',
    'sizeof','static','struct','switch','true','using','void','while'
    ,'std'
}

token_specification = [
    ('COMMENT',  r'//[^\n]*|/\*[\s\S]*?\*/'),
    ('PREPROC',  r'\#.*'), 
    ('FLOAT',    r'\d+\.\d*'),      
    ('INT',      r'\d+'),                        
    ('CHAR',     r"'(\\[abfnrtv0'\"?]|[^\\'])'"), 
    ('STRING',   r'"([^\\"]|\\.)*"'),            
    ('SEPARATOR',r'[\(\)\{\}\[\];,\.]'),         
    ('OPERATOR', r'\+\+|--|==|!=|<=|>=|<<=|>>=|->'
                 r'|\+=|-=|\*=|/=|%=|&=|\|=|\^='
                 r'|<<|>>|&&|\|\||~|!|\+|-|\*|/|%|='
                 r'|<|>|&|\||\^|\?|:'),         
    ('ID',       r'[A-Za-z_][A-Za-z0-9_]*'),      
    ('NEWLINE',  r'\n'),                         
    ('SKIP',     r'[ \t\r]+'),                   
    ('MISMATCH', r'.'),                          
]


master_pattern = re.compile(
    '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification),
    re.MULTILINE
)


def tokenize(code: str):
    """
    Generator yielding (kind, value, line) for each token,
    including comments.
    """
    line_num = 1

    for mo in master_pattern.finditer(code):
        kind  = mo.lastgroup
        value = mo.group()

        # 1) Skip only pure whitespace
        if kind == 'SKIP':
            continue

        # 2) Track newlines
        if kind == 'NEWLINE':
            line_num += 1
            continue

        # 3) Yield comments instead of skipping them
        if kind == 'COMMENT':
            yield 'COMMENT', value, line_num
            continue

        # 4) Preprocessor directives
        if kind == 'PREPROC':
            yield 'PREPROC', value.strip(), line_num
            continue

        # 5) Anything unrecognized
        if kind == 'MISMATCH':
            yield 'UNKNOWN', value, line_num
            continue

        # 6) Reclassify identifiers as keywords when appropriate
        if kind == 'ID' and value in KEYWORDS:
            kind = 'KEYWORD'

        # 7) Finally, yield all other tokens
        yield kind, value, line_num


def main():
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} <input.cpp> <output.txt>')
        sys.exit(1)

    input_path, output_path = sys.argv[1], sys.argv[2]
    with open(input_path, 'r', encoding='utf-8') as f:
        code = f.read()

    with open(output_path, 'w', encoding='utf-8') as out:
        for kind, value, line in tokenize(code):
            out_line = f'{kind} | {value} | {line}\n'
            out.write(out_line)
            print(out_line, end='')

if __name__ == '__main__':
    main()
