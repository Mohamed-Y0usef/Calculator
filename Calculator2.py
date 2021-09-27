class Calculator:
    
    def __init__(self , number1 , number2 , operator): 
        self.number1 = number1
        self.number2 = number2
        self.operator = operator
    
    def Sum (self):
        return self.number1 + self.number2 
     
    def Sub (self):
        return self.number1 - self.number2
    
    def Multiplay (self):
       return self.number1 * self.number2
        
    def Div (self):
        return self.number1 / self.number2
    
    def Pow (self): 
        number = 1
        for x in range(self.number2): 
            number = number * self.number1 
        return number 
    def op(self):
        return self.operator
        
i = "y"
while i == "y": 
    number1 = int(input ("Enter the first number : "))
    operator = input ("Enter the operator : ")
    number2 = int(input ("Enter the second number : "))
    C = Calculator(number1 , number2 , operator)
    
    if operator == "+":
        print(C.Sum())
    elif operator == "-":
        print(C.Sub())
    elif operator == "*":
        print(C.Multiplay())
    elif operator == "/":
        print(C.Div())
    elif operator == "^":
        print(C.Pow())
    
    i = input("press 'y' if you want to calculate again and press 'n' if you want to stop : ")