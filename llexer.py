import sys
from ltoken import LToken

class LLexer():
    def __init__(self):
        self.curr_char = sys.stdin.read(1)

    def next_char(self):
        self.curr_char = sys.stdin.read(1)

    def get_next_token(self):

        # single char token
        if (
            curr_char == LToken.PLUS
            or curr_char == LToken.MINUS
            or curr_char == LToken.MULT
            or curr_char == LToken.LPAREN
            or curr_char == LToken.RPAREN
            or curr_char == LToken.ASSIGN
            or curr_char == LToken.SEMICOL
            ):
            return curr_char
        
        # check multi char tokens
        
        # INT : [0-9]+
        if self.curr_char.isdigit():
            self.read_number()

        # END, PRINT, ID
        if curr_char.isalpha():
            str_literal = ""
            while curr_char.isalpha():
                str_literal += curr_char
                curr_char = sys.stdin.read(1)

            
            if len(str_literal) == 3:
                # END
                if str_literal[0] == "e" and str_literal[1] == "n" and str_literal[2] == "d":
                    return LToken.END
                
                # PRINT
                elif str_literal[0] == "p" and str_literal[1] == "r" and str_literal[2] == "i" and str_literal[3] == "i" and str_literal[2] == "t":
                    return LToken.END

            # ID
            return str_literal
        
        return LToken.ERROR
    
    def read_number(self):
        lexeme = ""
        while self.curr_char.isdigit():
            lexeme += self.curr_char
            self.next_char()
        return LToken(lexeme, LToken.INT)


    def skip_whitespace(self):
        while self.curr_char.isspace():
            self.next_char()

    