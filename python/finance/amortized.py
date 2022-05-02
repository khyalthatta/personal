# Step 1 : Find the annual payment using pvifa table
i = int(input("\n Interest Rate (in %) "))
i = i / 100
n = int(input("\n Number of years "))
pva = int(input("\n Borrow Amount(PVA) "))

pvifa = (1 - (1 / (1 + i) ** n))/i

pmt = pva / pvifa


def amortized_table(pmt, i, n,  pva):

    total_interest = 0
    principal_list = []
    interest_list = []
    for num in range(0, n+1):

        if num == 0:

            print(f""" Year         --> {num}
                        Payment         --> 0
                        Interest        --> 0
                        Principal       --> 0
                        Loan Balance    --> {pva} """)
        else:

            # Step 2 : Find  the interest paid in year 1
            interest = pva * i
            interest_list.append(interest)
            # Step 3 : Find  the principal re-paid in year 1
            principal = pmt - interest
            principal_list.append(principal)

            # Step 4 : Find  the ending balance after year 1
            loan_bal = pva - principal

            print(f""" Year         --> {num}
                       Payment      --> {pmt:.2f}
                       Interest     --> {interest:.2f}
                       Principal    --> {principal:.2f}
                       Loan Balance --> {loan_bal:.2f} """)

            pva = loan_bal

            total_interest += interest

    choice = input("""\n Choose the following keyword to calculate
    'pp' for percentage of principal
    'ip' for interest percentage
    'ti' for total of interest """)

    if choice.lower() == 'pp':

        def calc_fraction(principal_list):
            year = int(input("\n Enter the year to calculate principal(%) "))
            principal_fraction = (principal_list[year-1]/pmt) * 100
            return f"\n The percentage of principal in year {year} = {principal_fraction}"

        print(calc_fraction(principal_list))

    elif choice.lower() == 'ip':
        def calc_interest(interest_list):
            year = int(input("\n Enter the year to calculate interest of  "))
            interest_percentage = (interest_list[year - 1]/pmt) * 100
            return f"\n The percentage of interest in year {year} = {interest_percentage}"

        print(calc_interest(interest_list))

    elif choice.lower() == 'ti':
        print(f"Total Interest is {total_interest}")

    else:
        print("Error Occured!!")


amortized_table(pmt, i, n,  pva)
