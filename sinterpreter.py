import sys
from lparser import LParser

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
            line = self.get_next_line()
            
    def process_line(self, line):
        """ Process a single line of intermediate code """
        operator = line.split()[0]

        if operator == "PUSH":
            parts = line.split()
            if len(parts) != 2:
                self.error(operator)
            # push the lexeme onto the stack
            self.stack.append(parts[1])
        
        elif operator in LParser.STACK_OPERATORS.values():
            self.execute_operator(operator)

        else:
            self.error(operator)

    def resolve(self, item):
        # already an int
        if isinstance(item, int):
            return item

        str_item = item.strip()  # num or variable name)

        # if it's a num return it
        if str_item.lstrip("-").isdigit():
            return int(str_item)

        # otherwise it's a variable name (default = 0)
        return int(self.variables.get(str_item, 0))

    def execute_operator(self, operator=None):
        """ Execute the given operator (ADD, SUB, MULT, ASSIGN, PRINT) on the stack """
        if operator is None:
            return

        elif operator == "ADD":
            if len(self.stack) < 2:
                self.error(operator)
            right = self.resolve(self.stack.pop())
            left  = self.resolve(self.stack.pop())
            self.stack.append(left + right)   # push int result

        elif operator == "SUB":
            if len(self.stack) < 2:
                self.error(operator)
            right = self.resolve(self.stack.pop())
            left  = self.resolve(self.stack.pop())
            self.stack.append(left - right)   # push int result

        elif operator == "MULT":
            if len(self.stack) < 2:
                self.error(operator)
            right = self.resolve(self.stack.pop())
            left  = self.resolve(self.stack.pop())
            self.stack.append(left * right)   # push int result

        elif operator == "ASSIGN":
            if len(self.stack) < 2:
                self.error(operator)
            value_item = self.stack.pop()
            var_name   = self.stack.pop()

            # var_name must be a name, not a number
            if isinstance(var_name, int) or str(var_name).lstrip("-").isdigit():
                self.error(operator)

            value = self.resolve(value_item)
            self.variables[str(var_name)] = value

        elif operator == "PRINT":
            if len(self.stack) < 1:
                self.error(operator)
            item = self.stack.pop()
            print(self.resolve(item))

        else:
            self.error(operator)


    def error(self, name_of_operator):
        print(f"Error for operator: {name_of_operator}")
        sys.exit(0)


    
def main():
    interpreter = SInterpreter()
    interpreter.cycle()


if __name__ == "__main__":
    main()