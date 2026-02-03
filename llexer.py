import sys
from ltoken import LToken

class LLexer():
    def __init__(self):
        self.curr_char = sys.stdin.read(1)

    def next_char(self):
        self.curr_char = sys.stdin.read(1)


    def get_next_token(self):
        self.skip_whitespace()

        if self.curr_char == "":
            return LToken("", LToken.END)

        # read INT
        if self.curr_char.isdigit():
            return self.read_number()

        # read END, PRINT, ID
        if self.curr_char.isalpha():
            return self.read_identifier_or_keyword()
        
        
        # single char token
        if self.curr_char == '+':
            self.next_char()
            return LToken('+', LToken.PLUS)

        if self.curr_char == '-':
            self.next_char()
            return LToken('-', LToken.MINUS)

        if self.curr_char == '*':
            self.next_char()
            return LToken('*', LToken.MULT)

        if self.curr_char == '(':
            self.next_char()
            return LToken('(', LToken.LPAREN)

        if self.curr_char == ')':
            self.next_char()
            return LToken(')', LToken.RPAREN)

        if self.curr_char == '=':
            self.next_char()
            return LToken('=', LToken.ASSIGN)

        if self.curr_char == ';':
            self.next_char()
            return LToken(';', LToken.SEMICOL)

        # ERROR - unknown guy
        unknown_char = self.curr_char
        self.next_char()
        return LToken(unknown_char, LToken.ERROR)
    
    def read_number(self):
        """ INT : [0-9]+ """
        lexeme = ""
        while self.curr_char.isdigit():
            lexeme += self.curr_char
            self.next_char()
        return LToken(lexeme, LToken.INT)

    def read_identifier_or_keyword(self):
        """
        token = END - lexeme = end
        token = PRINT - lexeme = print
        """
      
        lexeme = ""
        while self.curr_char.isalpha():
            lexeme += self.curr_char
            self.next_char()

        if lexeme == "print":
            return LToken(lexeme, LToken.PRINT)
        elif lexeme == "end":
            return LToken(lexeme, LToken.END)
        else:
            return LToken(lexeme, LToken.ID)

    def skip_whitespace(self):
        while self.curr_char.isspace():
            self.next_char()

    
