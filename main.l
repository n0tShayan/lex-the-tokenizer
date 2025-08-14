%{
#include <stdio.h>
int line_num = 1;
%}

/* ---------- C++ Token Definitions ---------- */

KEYWORD     int|char|bool|float|long|short|double|string|signed|unsigned|break|case|class|const|continue|default|delete|do|else|enum|false|for|friend|if|namespace|new|private|protected|public|return|sizeof|static|struct|switch|true|using|void|while
ID          [a-zA-Z_][a-zA-Z0-9_]*
FLOAT       [0-9]+\.[0-9]*([eE][-+]?[0-9]+)?
INT         [0-9]+
CHAR        \'(\\[abfnrtv0\'\"\\?]|[^\\'])\'
STRING      \"([^\\\"]|\\.)*\"
COMMENT     (\/\/[^\n]*|\/\*([^*]|\*+[^*/])*\*+\/)
PREPROC     \#.*

SEPARATOR   [\(\)\{\}\[\];,\.]
OPERATOR    (\+\+|--|==|!=|<=|>=|<<=|>>=|->|\+=|-=|\*=|\/=|%=|&=|\|=|\^=|<<|>>|&&|\|\||~|!|\+|-|\*|\/|%|=|<|>|&|\||\^|\?|\:)

%%

{KEYWORD}       { printf("Line %d: Token = %s → Keyword\n", line_num, yytext); }
{ID}            { printf("Line %d: Token = %s → Identifier\n", line_num, yytext); }
{PREPROC}       { printf("Line %d: Token = %s → Preprocessor Directive\n", line_num, yytext); }

{SEPARATOR}     { printf("Line %d: Token = %s → Separator\n", line_num, yytext); }
{OPERATOR}      { printf("Line %d: Token = %s → Operator\n", line_num, yytext); }

{FLOAT}         { printf("Line %d: Token = %s → Float Literal\n", line_num, yytext); }
{INT}           { printf("Line %d: Token = %s → Integer Literal\n", line_num, yytext); }
{CHAR}          { printf("Line %d: Token = %s → Char Literal\n", line_num, yytext); }
{STRING}        { printf("Line %d: Token = %s → String Literal\n", line_num, yytext); }

{COMMENT}       { /* skip comments */ }
\n              { line_num++; }
[ \t\r]+        { /* ignore whitespace */ }

.               { printf("Line %d: Token = %s → Unknown or Unhandled\n", line_num, yytext); }

%%

int main() {
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}
