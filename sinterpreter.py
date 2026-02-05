import sys

class SInterpreter:
    def __init__(self):
        self.stack = []
        self.variables = {}

    def get_next_line(self):
        return sys.stdin.readline().strip()

    def cycle(self):
        line = self.get_next_line()
        while line:
            self.process_line(line)
            

    def process_line(self, line):
        x, token, y, lexeme = line.split()


    def error(self, name_of_operator):
        print(f"Error for operator: {name_of_operator}")
        exit(1)

    
def main():
    interpreter = SInterpreter()
    interpreter.cycle()
