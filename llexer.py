import sys
from ltoken import LToken

class LLexer():
    def __init__(self):
        self.curr_char = sys.stdin.read(1)

    def next_char(self):
        self.curr_char = sys.stdin.read(1)

    def read_single_char(self):
        if self.curr_char == LToken.PLUS:
            return LToken(self.curr_char, LToken.PLUS)
        if self.curr_char == LToken.MINUS:
            return LToken(self.curr_char, LToken.MINUS)
        if self.curr_char == LToken.MULT:
            return LToken(self.curr_char, LToken.MULT)
        if self.curr_char == LToken.LPAREN:
            return LToken(self.curr_char, LToken.LPAREN)
        if self.curr_char == LToken.RPAREN:
            return LToken(self.curr_char, LToken.RPAREN)
        if self.curr_char == LToken.ASSIGN:
            return LToken(self.curr_char, LToken.ASSIGN)
        if self.curr_char == LToken.SEMICOL:
            return LToken(self.curr_char, LToken.SEMICOL)


    def get_next_token(self):

        # single char token
        self.read_single_char()

        
        # check multi char tokens
        
        if self.curr_char.isdigit():
            self.read_number()

        if self.curr_char.isalpha():
            self.read_keyword()

        # ERROR
        return LToken(self.curr_char, LToken.ERROR)
    
    def read_number(self):
        """ INT : [0-9]+ """
        lexeme = ""
        while self.curr_char.isdigit():
            lexeme += self.curr_char
            self.next_char()
        return LToken(lexeme, LToken.INT)

    def read_keyword(self):
        """
        token = END - lexeme = end
        token = PRINT - lexeme = print
        """

        # END, PRINT, ID
        lexeme = ""
        while curr_char.isalpha():
            lexeme += curr_char
            curr_char = sys.stdin.read(1)

        
        if len(lexeme) == 3:
            # END
            if lexeme[0] == "e" and lexeme[1] == "n" and lexeme[2] == "d":
                return LToken(lexeme, LToken.END)
            
            # PRINT
            elif lexeme[0] == "p" and lexeme[1] == "r" and lexeme[2] == "i" and lexeme[3] == "i" and lexeme[2] == "t":
                return LToken(lexeme, LToken.PRINT)

        # ID
        return LToken(lexeme, LToken.ID)

    def skip_whitespace(self):
        while self.curr_char.isspace():
            self.next_char()

    