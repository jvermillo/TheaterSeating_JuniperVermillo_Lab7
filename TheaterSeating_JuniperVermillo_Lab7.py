def ticketSales():
    ticketSales = input("How many tickets were sold for this section? ")

    try:
        return int(ticketSales)
    except ValueError:
        print("Invalid input. Re-enter how many tickets were sold. ")

def sectionIncome(seating, price):
    tickets = ticketSales()

    while price < 0 or tickets > seating:
        print("Invalid input. Re-enter your the number of seats. ")
        tickets = ticketSales()

    sectionIncome = tickets * price

    return sectionIncome

def main():
    # Section prices
    A_PRICE = 20
    B_PRICE = 15
    C_PRICE = 10

    # Section seating capacity
    A_SEATING = 300
    B_SEATING = 500
    C_SEATING = 200

    # Print Theater Seating Info
    print("A dramatic theater has three seating sections, and it charges the following prices for tickets in each section: section A seats cost $20 each, section B seats cost $15 each, and section C seats cost $10 each. The theater has 300 seats in section A, 500 seats in section B, and 200 seats in section C. Enter how many seats were sold for each section. ")

    # Calculate Subtotals
    A_subtotal = sectionIncome(A_SEATING, A_PRICE)
    B_subtotal = sectionIncome(B_SEATING, B_PRICE)
    C_subtotal = sectionIncome(C_SEATING, C_PRICE)

    # Total price
    print(f"The total price is {A_subtotal + B_subtotal + C_subtotal}.")

main()