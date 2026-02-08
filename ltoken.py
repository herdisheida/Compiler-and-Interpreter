class LToken():

    ID = 0
    ASSIGN = 1
    SEMICOL = 2
    INT = 3
    PLUS = 4
    MINUS = 5
    MULT = 6
    LPAREN = 7
    RPAREN = 8
    PRINT = 9
    END = 10
    ERROR = 11

    ERROR = -1  # any other token

    def __init__(self, lexeme, token):
        self.lexeme = lexeme
        self.token_code = token

    def __str__(self):
        return f"Token: {self.token_code} Lexeme: {self.lexeme}"
        # return f"{self.lexeme}"
    
    def is_operator(self):
        return self.token_code in {LToken.PLUS, LToken.MINUS, LToken.MULT, LToken.ASSIGN}
    
    def is_variable(self):
        return self.token_code in {LToken.ID, LToken.INT}
