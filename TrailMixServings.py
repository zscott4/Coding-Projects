# Zoe Scott, 08-30-2022
# 1. Prints a welcome message
# 2. Takes input from the user on the number of servings they want (as a number)
# 3. Calculates the new ingredient quantities based on the input
# 4. Prints the new ingredient list with adjusted quantities.

print ("Hello! Let's make trail mix!")
TMservings = input("How many servings would you like?") # Asking how many trail mix servings the user would like

TMservingsint = (int(TMservings)) # Turning string into interger

print (TMservings, "Trail mix requires:")

cupsofPeanuts = TMservingsint * 2         # Ingredients conversions for desired serving size
cupsofRaisins = TMservingsint / 2
cupsofMM = TMservingsint * 1.5

print (cupsofPeanuts, "cups of peanuts") # Amount of ingredients per serving
print (cupsofRaisins, "cups of raisins")
print (cupsofMM, "spoons of M&Ms")

