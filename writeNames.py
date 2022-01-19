import pandas as pd

filename = "66th-Induction-List-Final.xlsx"
names = pd.read_excel(filename, sheet_name="lastNameOrder")

induction_number = 66

with open("sorted_names.txt", "w") as write_file:
    for i in range(1, len(names["Last Name"])):
        write_file.write(f"{induction_number},\"{names['First Name'][i]} {names['Last Name'][i]}\",false\n")

print("done!")
