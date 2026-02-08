from ltoken import LToken
import sys

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
        print ("Syntax error")
        sys.exit(0)


    def statements(self):
        """ start symbol,
        Statements -> Statement ; Statements | end
        """

        # end
        if self.curr_token.token_code == LToken.END:
            return

        # Statement ; Statement
        self.statement()

        if self.curr_token.token_code != LToken.SEMICOL:
            return self.error()
            
        self.next_token() # consume ;
        return self.statements()
        

    def statement(self):
        """ Statement -> id = Expr | print id """
        if self.curr_token.token_code == LToken.ID:
            print("PUSH", self.curr_token.lexeme)

            self.next_token() # consume id
            if self.curr_token.token_code != LToken.ASSIGN:
                return self.error()
            
            self.next_token() # consume =
            self.expr()
            print("ASSIGN")
            return

        if self.curr_token.token_code == LToken.PRINT:
            self.next_token()  # consume print
            if self.curr_token.token_code != LToken.ID:
                return self.error()
            print("PUSH", self.curr_token.lexeme)
            self.next_token()  # consume id
            print("PRINT")
            return
            
        return self.error()
            

    def expr(self):
        """ Expr -> Term | Term + Expr | Term - Expr """
        self.term()

        if self.curr_token.token_code == LToken.PLUS:
            self.next_token()  # consume +
            self.expr()
            print("ADD")
            return

        if self.curr_token.token_code == LToken.MINUS:
            self.next_token()  # consume -
            self.expr()
            print("SUB")
            return
        

    def term(self):
        """ Term -> Factor | Factor * Term """
        self.factor()

        if self.curr_token.token_code == LToken.MULT:
            self.next_token()  # consume *
            self.term()
            print("MULT")
            return


    def factor(self):
        """ Factor -> int | id | ( Expr ) """
        if self.curr_token.token_code == LToken.INT:
            print("PUSH", self.curr_token.lexeme)
            self.next_token()
            return

        if self.curr_token.token_code == LToken.ID:
            print("PUSH", self.curr_token.lexeme)
            self.next_token()
            return

        if self.curr_token.token_code == LToken.LPAREN:
            self.next_token()  # consume (
            self.expr()
            if self.curr_token.token_code != LToken.RPAREN:
                return self.error()
            self.next_token()  # consume )
            return
        
        # not int, id, or (
        return self.error()
