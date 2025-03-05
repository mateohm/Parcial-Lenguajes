# Generated from Complex.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ComplexParser import ComplexParser
else:
    from ComplexParser import ComplexParser

# This class defines a complete listener for a parse tree produced by ComplexParser.
class ComplexListener(ParseTreeListener):

    # Enter a parse tree produced by ComplexParser#expr.
    def enterExpr(self, ctx:ComplexParser.ExprContext):
        pass

    # Exit a parse tree produced by ComplexParser#expr.
    def exitExpr(self, ctx:ComplexParser.ExprContext):
        pass


    # Enter a parse tree produced by ComplexParser#complex.
    def enterComplex(self, ctx:ComplexParser.ComplexContext):
        pass

    # Exit a parse tree produced by ComplexParser#complex.
    def exitComplex(self, ctx:ComplexParser.ComplexContext):
        pass



del ComplexParser