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


    def Statements(self):
        """ start symbol,
        Statements -> Statement ; Statements | end
        """
        pass

    def statement(self):
        """ Statement -> id = Expr | print id """
        # statement starts with id or print, so we can check the current token to decide which production to use
        if self.curr_token.token_code == LToken.ID:
            curr_id = self.curr_token.lexeme
            self.next_token() # consume id
            if self.curr_token.token_code != LToken.ASSIGN:
                self.error() # dumymy error function
                print("syntax error")
            self.next_token() # consume =
            self.Expr()
            return f"{curr_id} = {self.Expr()}"

        elif self.curr_token.token_code == LToken.PRINT:
            self.next_token() # consume print
            if self.curr_token.token_code != LToken.ID:
                self.error()
                print("syntax error")
            curr_id = self.curr_token.lexeme
            self.next_token() # consume id
            return f"print {curr_id}"
        else:
            self.error() # dummy error function
            print("syntax error")
            
            
            

    def expr(self):
        """ Expr -> Term | Term + Expr | Term - Expr """
        if self.curr_token.token_code == LToken.INT or self.curr_token.token_code == LToken.ID or self.curr_token.token_code == LToken.LPAREN:
            left = self.Term()
            while self.curr_token.token_code == LToken.PLUS or self.curr_token.token_code == LToken.MINUS:
                operator = self.curr_token.lexeme
                self.next_token()
                right = self.Term()
                left = f"({left} {operator} {right})"
            return left
        else:
            self.error()
            print("syntax error")

    def Term(self):
        """ Term -> Factor | Factor * Term """
        pass

    def Factor(self):
        """ Factor -> int | id | ( Expr ) """
        pass