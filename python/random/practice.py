import pandas as pd

columns = ['name', 'club', 'kit_no']

df = pd.DataFrame(columns = columns)

while True:

    name = input("Enter name of a player ")
    club = input("Enter name of a club ")
    kit_no = input("Enter shirt no of a player ")

    df = df.append({'name': name , 'club': club, 'kit_no': kit_no}, ignore_index = True)


    another = input("Add Anothe? y/n ")

    if another.lower() == 'y':
        continue

    elif another.lower() == 'n':
        break

    else:
        print(" You have typed wrong keyword. Please try again!! ")
        break


print(df)
