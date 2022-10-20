import sys
def welcome(): #welcome function
    print("Welcome! Here is some important information about the benefits of the Vitamins.")
def ValidInput(): 
        while True:
            x = int(input("Please enter number from 1 to 5 or 0 if you want to quit:")) #user enters 1,2,3,4,5 or 0
            if x == 1:
                print("Vitamin A protects eyes from night blindness and age-related decline") #option1
                
            if x == 2:
                print("Vitamin B6 promotes brain health and reduces Alzheimer's risk")#option2
                
            elif x == 3:
                print("Vitamin B12 may improve heart health by decreasing homocysteine") #option3
                
            elif x == 4:
                print("Vitamin C protects your health from cardiovascular issues, cancer, and strokes") #option4
                
            elif x == 5:
                print("Vitamin D reduces the risk of diabetes") #option5
                
            elif x == 0:
                print("Good-bye!") #option6 (0)
                sys.exit() #terminates the function
            else:
                print("Invalid number! Please enter number from 1 to 5")
def main():    
    welcome() #calls welcome function
    ValidInput() #calls validinput function
main()