class BMI:

    def __init__(self, name, age, weight, height): 
        self.name   = name
        self.age    = age
        self.weight = weight
        self.height = height
    
    def solve_BMIself(self):
        BMI = self.weight / (self.height/100)**2
        if BMI <= 18.4:
           return print("You are underweight.")
        elif BMI <= 24.9:
           return print("You are healthy.")
        elif BMI <= 29.9:
           return print("You are over weight.")
        elif BMI <= 34.9:
           return print("You are severely over weight.")
        elif BMI <= 39.9:
           return print("You are obese.")
        else:
           return print("You are severely obese.")

        print(f"your BMI is {BMI}")
      

person_1 = BMI("Karl", 12, 54, 54)

person_1.solve_BMIself()




    