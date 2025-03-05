from antlr4 import *
from ComplexLexer import ComplexLexer
from ComplexParser import ComplexParser

def evaluar_expresion(expresion):
    lexer = ComplexLexer(InputStream(expresion))
    stream = CommonTokenStream(lexer)
    parser = ComplexParser(stream)
    tree = parser.expr()
    print("Expresión válida:", expresion)

entrada = "(3+4i) + (2-5i)"
evaluar_expresion(entrada)
