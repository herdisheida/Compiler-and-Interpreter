class SInterpreter:
    def __init__(self):
        self.stack = []
        self.variables = {}


    def cycle(self):
        pass


    def error(self, name_of_operator):
        print(f"Error for operator: {name_of_operator}")
        exit(1)

    
def main():
    interpreter = SInterpreter()
    interpreter.cycle()
