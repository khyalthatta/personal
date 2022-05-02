# Calculation of uneven cash flow of present value.


# Step 1 : Insertation of interest.

i = float(input("\n Enter the rate of interest (in %) "))
i = i / 100

# Step 2 : Insertation of range of year on a list.

print("\n Enter the range of year (1 to 5) ")

n = []
for num in range(0, 2):
    n.append(int(input(" ")))

# Step 3 : Insertation of cash flow on a list.

print("\n Enter the cash flow ")

cash_flow = {}
for num in range(n[0],  n[1]+1):
    cash_flow[num] = int(input(" "))

# Step 4 : Create a function that calculate the value of a cash flow.


def calc_uneven_pv(cash_flow, i, n):

    pv = 0

    for num in range(n[0],  n[1]+1):
        pvif = (1/(1 + i) ** num)
        pv += pvif * cash_flow[num]

    return pv


print(f"The present value of the uneven cash flow is {calc_uneven_pv(cash_flow, i, n):.2f}")
