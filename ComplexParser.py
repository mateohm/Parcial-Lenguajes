# Generated from Complex.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,9,32,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,1,0,1,0,3,0,11,8,0,1,0,
        1,0,1,0,1,0,1,0,1,0,5,0,19,8,0,10,0,12,0,22,9,0,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,30,8,1,1,1,0,1,0,2,0,2,0,2,1,0,1,2,1,0,3,4,33,0,10,1,
        0,0,0,2,29,1,0,0,0,4,5,6,0,-1,0,5,6,5,5,0,0,6,7,3,0,0,0,7,8,5,6,
        0,0,8,11,1,0,0,0,9,11,3,2,1,0,10,4,1,0,0,0,10,9,1,0,0,0,11,20,1,
        0,0,0,12,13,10,4,0,0,13,14,7,0,0,0,14,19,3,0,0,5,15,16,10,3,0,0,
        16,17,7,1,0,0,17,19,3,0,0,4,18,12,1,0,0,0,18,15,1,0,0,0,19,22,1,
        0,0,0,20,18,1,0,0,0,20,21,1,0,0,0,21,1,1,0,0,0,22,20,1,0,0,0,23,
        24,5,8,0,0,24,25,7,0,0,0,25,26,5,8,0,0,26,30,5,7,0,0,27,28,5,8,0,
        0,28,30,5,7,0,0,29,23,1,0,0,0,29,27,1,0,0,0,30,3,1,0,0,0,4,10,18,
        20,29
    ]

class ComplexParser ( Parser ):

    grammarFileName = "Complex.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'", 
                     "'i'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUM", "WS" ]

    RULE_expr = 0
    RULE_complex = 1

    ruleNames =  [ "expr", "complex" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    NUM=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ComplexParser.ExprContext)
            else:
                return self.getTypedRuleContext(ComplexParser.ExprContext,i)


        def complex_(self):
            return self.getTypedRuleContext(ComplexParser.ComplexContext,0)


        def getRuleIndex(self):
            return ComplexParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ComplexParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.state = 5
                self.match(ComplexParser.T__4)
                self.state = 6
                self.expr(0)
                self.state = 7
                self.match(ComplexParser.T__5)
                pass
            elif token in [8]:
                self.state = 9
                self.complex_()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 20
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 18
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ComplexParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 12
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 13
                        _la = self._input.LA(1)
                        if not(_la==1 or _la==2):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 14
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = ComplexParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 15
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 16
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 17
                        self.expr(4)
                        pass

             
                self.state = 22
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComplexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(ComplexParser.NUM)
            else:
                return self.getToken(ComplexParser.NUM, i)

        def getRuleIndex(self):
            return ComplexParser.RULE_complex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplex" ):
                listener.enterComplex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplex" ):
                listener.exitComplex(self)




    def complex_(self):

        localctx = ComplexParser.ComplexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_complex)
        self._la = 0 # Token type
        try:
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(ComplexParser.NUM)
                self.state = 24
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 25
                self.match(ComplexParser.NUM)
                self.state = 26
                self.match(ComplexParser.T__6)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(ComplexParser.NUM)
                self.state = 28
                self.match(ComplexParser.T__6)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




