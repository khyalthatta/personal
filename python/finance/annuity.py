payment = float(input("\n Enter payment: "))
rate = float(input("\n Enter rate of return: "))
year = float(input("\n Enter year: "))
rate = rate/100


def calc_annuity(payment, rate, year):

    value = input("Enter the value you want to calculate. future or present? ")
    if value.lower() == 'present':
        annuity = input("Enter the types of annuity. ordinary or due? ")

        if annuity.lower() == 'ordinary':
            ordinary_annuity = payment * ((1 - (1 / (1 + rate) ** year))/rate)
            return ordinary_annuity

        elif annuity.lower() == 'due':
            annuity_due = payment * ((1 - (1 / (1 + rate) ** year))/rate) * (1 + rate)
            return annuity_due

        else:
            return "The keyword you have passed is wrong. Please try with right one."

    elif value.lower() == 'future':

        annuity = input("Enter the types of annuity. ordinary or due? ")

        if annuity.lower() == 'ordinary':
            ordinary_annuity = payment * (((1 + rate) ** year)-1)/rate
            return ordinary_annuity

        elif annuity.lower() == 'due':
            annuity_due = payment * (((1 + rate) ** year)-1)/rate * (1 + rate)
            return annuity_due

        else:
            return "The keyword you have passed is wrong. Please try with right one."

    else:
        return "You have to type the keyword correctly."


print(f"{calc_annuity(payment, rate, year): .2f}")
