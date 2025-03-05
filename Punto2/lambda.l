%{
#include <stdio.h>
%}

DIGIT  [0-9]+
ID     [a-zA-Z_][a-zA-Z0-9_]*
LAMBDA "lambda"
EXP    "**"

%%

{ID}      { printf("IDENTIFICADOR: %s\n", yytext); }
{LAMBDA}  { printf("PALABRA CLAVE: lambda\n"); }
{EXP}     { printf("OPERADOR: **\n"); }
{DIGIT}   { printf("NUMERO: %s\n", yytext); }
"="       { printf("ASIGNACION: =\n"); }
":"       { printf("DOS PUNTOS: :\n"); }
"("       { printf("PARENTESIS IZQUIERDO: (\n"); }
")"       { printf("PARENTESIS DERECHO: )\n"); }

\n|\t| " "  { /* Ignorar espacios y saltos de línea */ }

.         { printf("ERROR: Caracter desconocido: %s\n", yytext); }

%%

int main(int argc, char **argv) {
    yylex();
    return 0;
}
