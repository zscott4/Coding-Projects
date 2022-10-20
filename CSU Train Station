def main(): #define main
    def welcome(): #staring welcome function
        print("Welcome to the CSU Train Station!")
        print("""Tickets are $60.98 each
        Each bad charge is an extra $5.25
        Beverages are $1.99 each""")
    welcome()
    q = float(input("How many tickets do you need?"))
    r = float(input("How many bags do you have?"))
    def TotalTickets(x):
        totaltix = x * 60.98 #calculating total tickets
        return totaltix
    def TotalLuggage(y):
        totallug = y * 5.25 #calculating total luggage
        return totallug  
    TotalTickets(q)
    TotalLuggage(r)
    s = float(input("How many beverages would you like to have on this trip?"))
    def TotalBeverage(z):
        totalbev = z * 1.99 #calculating total beverages
        return totalbev
    TotalBeverage(s)
    def Salestax(a):
        tax = a * 1.08 #calculating subtotal with taxes
        tax1 = round(tax,2)
        return tax1
    subtotal = TotalBeverage(s) + TotalLuggage(r) + TotalTickets(q)
    subtotal1 = round(subtotal,2)
    print("Your subtotal is", subtotal1)
    print("Your total with tax is", Salestax(subtotal))
 #call main function   
main()
