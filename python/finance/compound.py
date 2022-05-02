investment = int(input("\n Enter the present value of an investment. "))
rate = float(input("\n Enter the required rate of return for the investment. "))
year = int(input("\n Enter the year for the investment. "))

while True:

    def calc_compound(investment, rate, year):

        period = int(input("""\n Please enter the period for the compunding interest
        1 for Annual
        2 for Semi Annual
        3 for Quarter
        4 for Month
        """))

        if period == 1:
            compound_interest = investment * (1 + rate/100) ** year
            return compound_interest

        elif period == 2:
            compound_interest = investment * (1 + rate/(100*2)) ** (year*2)
            return compound_interest

        elif period == 3:
            compound_interest = investment * (1 + rate/(100*4)) ** (year*4)
            return compound_interest

        elif period == 4:
            compound_interest = investment * (1 + rate/(100*12)) ** (year*12)
            return compound_interest

        else:
            return "not determined due to the wrong period."

    result = calc_compound(investment, rate, year)

    print(f"\n The compound interest for the investment is {result}")

    check_again = input("\n Would you like to check your investment on other period?yes/no ")

    if check_again.lower() == "yes":
        continue

    else:
        print("Done!!!")
        break
