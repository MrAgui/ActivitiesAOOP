# print("\nBMI calculator\n")

# print("Weight in centimeter and height in  kilograms\n")

# weight = float(input("Enter weight in kg: "))

# height = float(input("Enter height in cm: "))

# BMI = weight / (height/100)**2

# print(f"\nYour BMI is {BMI}\n")

# if BMI <= 18.4:
#     print("You are underweight.")
# elif BMI <= 24.9:
#     print("You are healthy.")
# elif BMI <= 29.9:
#     print("You are over weight.")
# elif BMI <= 34.9:
#     print("You are severely over weight.")
# elif BMI <= 39.9:
#     print("You are obese.")
# else:
#     print("You are severely obese.")
    

# class person(): 
#     def _init_(self, name, age, weight, height ):
#         self.name   = name
#         self.age    = age
#         self.weight = weight
#         self.height = height
    
#     def getInputFromUser(self):
#         name    = str("Name: ")
#         age     = int("Age: ")
#         weight  = float("Enter weight in kg: ")
#         height  = float("Enter height in cm: ")
  
#         return name, age, weight, height;  
    
#     def computeBMI():
#         BMI = weight / (height/100)**2
#         return BMI 
    
#     getInputFromUser(self)

# print(f"BMI of " + name + "is {BMI}")
# print("Im running")          

# class BMI:

#     def __init__(self, name, age, weight, height): 
#         self.name   = name
#         self.age    = age
#         self.weight = weight
#         self.height = height

#     @classmethod
#     def from_input(cls):
#         return cls(
#             name=  input("Name: "),
#             age =  float(input("Age: ")), 
#             weight = float(input("Weight: ")),
#             height  = float(input("Height: "))
#         )
#     @classmethod
#     def solveBMI(the_BMI):
#         # BMI =  weight / (height/100)**2
#         # if BMI <= 18.4:
#         #     print("You are underweight.")
#         # elif BMI <= 24.9:
#         #     print("You are healthy.")
#         # elif BMI <= 29.9:
#         #     print("You are over weight.")
#         # elif BMI <= 34.9:
#         #     print("You are severely over weight.")
#         # elif BMI <= 39.9:
#         #     print("You are obese.")
#         # else:
#         #     print("You are severely obese.")
#         # return BMI
#         return the_BMI(
#             BMI =  weight / (height/100)**2
#             if BMI <= 18.4;
#                 print("You are underweight.")
#             elif BMI <= 24.9:
#                 print("You are healthy.")
#             elif BMI <= 29.9:
#                 print("You are over weight.")
#             elif BMI <= 34.9:
#                 print("You are severely over weight.")
#             elif BMI <= 39.9:
#                 print("You are obese.")
#             else:
#                 print("You are severely obese.")
#             return BMI
#         )
        
    
# person = BMI.from_input().solveBMI()

## Goal creat a class about BMI calculator 

class BMI:

    def __init__(self, name, age, weight, height): 
        self.name   = name
        self.age    = age
        self.weight = weight
        self.height = height
    
    
person_1 = BMI("Karl", 12, 54, 54)

print(person_1.name + f"is{person_1.age} " )


    