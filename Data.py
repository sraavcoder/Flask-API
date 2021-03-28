from csv import reader

Data_rows = []
with open('Export.csv', 'r') as f:
    csv_reader = reader(f)
    for row in csv_reader:
        Data_rows.append(row)
del Data_rows[0]

final_list_Dwarf = []
final_list_Star = []
final_list = []

for planet_data in Data_rows:
    temp_dict3 = {
        "Brown_Dwarf_Name": planet_data[2],
        "Distance_BrownDwarf": planet_data[5],
        "Mass_BrownDwarf": planet_data[6],
        "Radius_BrownDwarf": planet_data[7],
        "Gravity_Dwarf": planet_data[8],
        "Star_name": planet_data[11],
        "Distance_Star": planet_data[12],
        "Mass_Star": planet_data[13],
        "Radius_Star": planet_data[14],
        "Gravity_Star": planet_data[15]
    }
    final_list.append(temp_dict3)

for planet_data in Data_rows:
    temp_dict = {
        "Brown_Dwarf_Name": planet_data[2],
        "Distance_BrownDwarf": planet_data[5],
        "Mass_BrownDwarf": planet_data[6],
        "Radius_BrownDwarf": planet_data[7],
        "Gravity_Dwarf": planet_data[8]
    }
    final_list_Dwarf.append(temp_dict)

for planet_data in Data_rows:
    temp_dict2 = {
        "Star_name": planet_data[11],
        "Distance_Star": planet_data[12],
        "Mass_Star": planet_data[13],
        "Radius_Star": planet_data[14],
        "Gravity_Star": planet_data[15]
    }
    final_list_Star.append(temp_dict2)
