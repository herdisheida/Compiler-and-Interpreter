import sys
from ltoken import LToken

class LLexer():
    def get_next_token():
        token = sys.stdin.read(1)

        # single char token
        if (
            token == LToken.PLUS
            or token == LToken.MINUS
            or token == LToken.MULT
            or token == LToken.LPAREN
            or token == LToken.RPAREN
            or token == LToken.ASSIGN
            or token == LToken.SEMICOL
            ):
            return token
        
        # check multi char tokens
        
        # INT : [0-9]+
        if token.isdigit():
            int_literal = ""
            while token.isdigit():
                int_literal += token
                token = sys.stdin.read(1)
            return int(int_literal)

        # END, PRINT, ID
        if token.isalpha():
            str_literal = ""
            while token.isalpha():
                str_literal += token
                token = sys.stdin.read(1)

            
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