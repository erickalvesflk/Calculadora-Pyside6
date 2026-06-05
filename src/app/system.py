
class CalcSystem(object):

    pseudo_operators = {
        "mod": "%",
        "x": "*",
        "÷": "/"
    }

    used_parenthesis = False

    def __init__(self):
        self.label = ""
        self.equation = ""
        
    def reset(self) -> str:
        self.label = ""
        self.equation = ""
        self.used_parenthesis = False
        return self.label

    def delete_c(self) -> str:
        if not self.label: return self.label

        if self.label[len(self.label)-1] == "d":
            self.label = self.label[:-3]
            self.equation = self.label[:-1]
            return self.label


        if self.label[len(self.label)-1] == "(":
            self.used_parenthesis = False

        self.label = self.label[:-1]
        self.equation = self.label[:-1]
        return self.label

    def add_to_op(self,s: str) -> str:

        if s == "()":
            if not self.used_parenthesis:
                self.used_parenthesis = True
                self.equation += "("
                self.label += "("
            else:
                self.used_parenthesis = False
                self.equation += ")"
                self.label += ")"

            return self.label

        self.label += s
        
        if not(s in self.pseudo_operators.keys()):
            self.equation += s
        else:
            self.equation += self.pseudo_operators[s]

        return self.label
    
    def result(self) -> str:

        if not self.equation: return self.equation

        try: 
            result = "R: " + str(eval(self.equation))
        except SyntaxError,TypeError:
            result = "Syntax Error"
        
        self.reset()
        return result
        