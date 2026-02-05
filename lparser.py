from ltoken import LToken
from llexer import LLexer

class LParser:

    def __init__(self):
        self.lexer = LLexer()
        self.curr_token = LToken()
        self.next_token() # first token

    def parse(self):
        self.next_token()
        self.statements()
        print() # Make sure the intermediate code ends with a newline

    def next_token(self):
        self.curr_token = self.lexer.get_next_token()
        if self.curr_token.token_code == LToken.ERROR:
            self.error()

    def error():
        pass # TODO

    def Statements(self):
        """ start symbol,
        Statements -> Statement ; Statements | end
        """

        # end
        if self.curr_token == self.END:
            return self.parse()

        # Statement ; Statement
        self.Statement()

        if self.curr_token != self.SEMICOL:
            self.curr_token.token_code == LToken.ERROR ## ERROR ERRROR
            print("Syntax error")

        self.parse() # parse SEMiCoL
        self.Statement()
        

    def Statement():
        """ Statement -> id = Expr | print id """
        pass

    def Expr():
        """ Expr- > Term | Term + Expr | Term - Expr """
        pass

    def Term():
        """ Term -> Factor | Factor * Term """
        pass

    def Factor():
        """ Factor -> int | id | ( Expr ) """
        pass