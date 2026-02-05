from ltoken import LToken
from llexer import LLexer

class LParser:

    def __init__(self, lexer):
        self.lexer = lexer
        self.curr_token = None

    def parse(self):
        self.next_token()
        self.statements()
        print() # Make sure the intermediate code ends with a newline

    def next_token(self):
        self.curr_token = self.lexer.get_next_token()
        if self.curr_token.token_code == LToken.ERROR:
            self.error()

    def error(self):
        print ("Syntax Error")
        exit(1)

    def statements(self):
        """ start symbol,
        Statements -> Statement ; Statements | end
        """

        # end
        if self.curr_token.token_code == LToken.END:
            print(self.curr_token)
            return self.next_token() # parse the end

        # Statement ; Statement
        self.statement()

        if self.curr_token.token_code != LToken.SEMICOL:
            return self.error()
            
        print(self.curr_token)
        self.next_token() # parse SEMiCoL
        return self.statements()
        

    def statement(self):
        """ Statement -> id = Expr | print id """
        # statement starts with id or print, so we can check the current token to decide which production to use
        if self.curr_token.token_code == LToken.ID:
            print(self.curr_token)
            self.next_token() # consume id
            if self.curr_token.token_code != LToken.ASSIGN:
                return self.error() # dumymy error function
            print(self.curr_token)
            self.next_token() # consume =
            self.expr()

        elif self.curr_token.token_code == LToken.PRINT:
            print(self.curr_token)
            self.next_token() # consume print
            if self.curr_token.token_code != LToken.ID:
                return self.error()
            print(self.curr_token)
            self.next_token() # consume id
            
        else:
            return self.error() # dummy error function
            
            
            

    def expr(self):
        """ Expr -> Term | Term + Expr | Term - Expr """
        self.term()

        if self.curr_token.token_code == LToken.PLUS:
            print(self.curr_token)
            self.next_token() # parse +
            self.expr()

        elif self.curr_token.token_code == LToken.MINUS:
            print(self.curr_token)
            self.next_token() # parse -
            self.expr()

        else:
            return


    def term(self):
        """ Term -> Factor | Factor * Term """
        self.factor()

        if self.curr_token.token_code == LToken.MULT:
            print(self.curr_token)
            self.next_token() # parse *
            self.term()


    def factor(self):
        """ Factor -> int | id | ( Expr ) """
        if self.curr_token.token_code == LToken.INT:
            print(self.curr_token)
            self.next_token() # parse int

        elif self.curr_token.token_code == LToken.ID:
            print(self.curr_token)
            self.next_token() # parse id

        elif self.curr_token.token_code == LToken.LPAREN:
            print(self.curr_token)
            self.next_token() # parse (
            self.expr()
            if self.curr_token.token_code != LToken.RPAREN:
                return self.error()
            print(self.curr_token)
            self.next_token() # parse )
        
        else:
            # not int, id, or (
            return self.error()