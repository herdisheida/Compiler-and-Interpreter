from ltoken import LToken
from llexer import LLexer

class LParser:

    OPERATORS = {
        LToken.PLUS: "ADD",
        LToken.MINUS: "SUB",
        LToken.MULT: "MULT",
        LToken.ASSIGN: "ASSIGN",
        LToken.PRINT: "PRINT"
    }

    def __init__(self, lexer):
        self.lexer = lexer
        self.curr_token = None

        self.operators = []
        self.variables = []

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


    def check_intermediate_line(self):
        """ Put operators and variable toknes into respective lists """
        if  self.curr_token.is_operator():
            self.operators.insert(0, self.curr_token)
        elif self.curr_token.is_variable():
            self.variables.append(self.curr_token)
        elif self.curr_token.token_code == LToken.PRINT:
            self.operators.insert(0, self.curr_token)

    def print_intermediate_line(self):
        """ Print the intermediate line  """
        for var in self.variables:
            print("PUSH", var, end='\n')
        for op in self.operators:
            print(self.OPERATORS[op.token_code], end='\n')
        self.variables = []
        self.operators = []


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
            return self.error()
            
        self.check_intermediate_line()
        self.next_token() # parse SEMiCoL

        self.print_intermediate_line()

        return self.statements()
        

    def statement(self):
        """ Statement -> id = Expr | print id """
        # statement starts with id or print, so we can check the current token to decide which production to use
        if self.curr_token.token_code == LToken.ID:
            self.check_intermediate_line()
            self.next_token() # consume id
            if self.curr_token.token_code != LToken.ASSIGN:
                return self.error() # dumymy error function
            self.check_intermediate_line()
            self.next_token() # consume =
            self.expr()

        elif self.curr_token.token_code == LToken.PRINT:
            self.check_intermediate_line()
            self.next_token() # consume print
            if self.curr_token.token_code != LToken.ID:
                return self.error()
            self.check_intermediate_line()
            self.next_token() # consume id
            
        else:
            return self.error()
            
            
            

    def expr(self):
        """ Expr -> Term | Term + Expr | Term - Expr """
        self.term()

        if self.curr_token.token_code == LToken.PLUS:
            self.check_intermediate_line()
            self.next_token() # parse +
            self.expr()

        elif self.curr_token.token_code == LToken.MINUS:
            self.check_intermediate_line()
            self.next_token() # parse -
            self.expr()

        else:
            return


    def term(self):
        """ Term -> Factor | Factor * Term """
        self.factor()

        if self.curr_token.token_code == LToken.MULT:
            self.check_intermediate_line()
            self.next_token() # parse *
            self.term()


    def factor(self):
        """ Factor -> int | id | ( Expr ) """
        if self.curr_token.token_code == LToken.INT:
            self.check_intermediate_line()
            self.next_token() # parse int

        elif self.curr_token.token_code == LToken.ID:
            self.check_intermediate_line()
            self.next_token() # parse id

        elif self.curr_token.token_code == LToken.LPAREN:
            self.check_intermediate_line()
            self.next_token() # parse (
            self.expr()
            if self.curr_token.token_code != LToken.RPAREN:
                return self.error()
            self.check_intermediate_line()
            self.next_token() # parse )
        
        else:
            # not int, id, or (
            return self.error()