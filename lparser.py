from ltoken import LToken
from llexer import LLexer

class LParser:

    def __init__(self, lexer):
        self.lexer = lexer
        self.curr_token = None
        self.next_token() # first token

    def parse(self):
        self.next_token()
        self.statements()
        print() # Make sure the intermediate code ends with a newline

    def next_token(self):
        self.curr_token = self.lexer.get_next_token()
        if self.curr_token.token_code == LToken.ERROR:
            self.error()

    def error(self):
        pass # TODO wat is dis ?

    def statements(self):
        """ start symbol,
        Statements -> Statement ; Statements | end
        """

        # end
        if self.curr_token.token_code == LToken.END:
            return self.next_token() # parse the end

        # Statement ; Statement
        self.statement()

        if self.curr_token.token_code != LToken.SEMICOL:
            self.curr_token.token_code == LToken.ERROR
            print("Syntax error")
            

        self.next_token() # parse SEMiCoL
        self.statements()
        

    def Statement():
        """ Statement -> id = Expr | print id """
        pass

    def Expr():
        """ Expr- > Term | Term + Expr | Term - Expr """
        pass

    def term(self):
        """ Term -> Factor | Factor * Term """
        self.factor()

        if self.curr_token.token_code == LToken.MULT:
            self.next_token() # parse *
            self.term()


    def factor(self):
        """ Factor -> int | id | ( Expr ) """
        if self.curr_token.token_code == LToken.INT:
            self.next_token() # parse int

        elif self.curr_token.token_code == LToken.ID:
            self.next_token() # parse id

        elif self.curr_token.token_code == LToken.LPAREN:
            self.next_token() # parse (
            self.expr()
            if self.curr_token.token_code != LToken.RPAREN:
                self.curr_token.token_code == LToken.ERROR
                print("Syntax error")
            self.next_token() # parse )
        
        else:
            # not int, id, or (
            self.curr_token.token_code == LToken.ERROR
            print("Syntax error")