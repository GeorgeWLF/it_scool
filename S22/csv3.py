import csv
import pathlib

root = pathlib.Path(__file__).parent
files_path = root.joinpath("files")

# citire fisier csv
lista_salarii = []
try:
    with open(files_path.joinpath("salarii.csv")) as fin:
        reader = csv.reader(fin) # csv.reader returneaza un generator, trebuie convertit la lista
        
except OSError:
    print("File error.")
else:
    for i in reader:
        print(i)

# citire fisier csv cu nume campuri
# field_names = [
#     "first_name",
#     "last_name",
#     "id",
#     "gros_salary",
#     "days_off"
# ]
# try:
#     with open(files_path.joinpath("salarii.csv")) as fin:
#         # list -> extrage datele din generator
#         dict_reader = list(csv.DictReader(fin, fieldnames=field_names))
#         for i in dict_reader:
            
# except OSError:
#     print("File error.")


# # scriere csv
# try:
#     with open(files_path.joinpath("net_salaries.csv"), "w") as fout:
#         csv_writer = csv.writer(fout)
#         for i in reader:
#             net = int(i[3]) * 0.65
#             csv_writer.writerow([i[0], i[1], net])
# except OSError:
#     print("File write error.")

# # csv.DictWriter - get a dict for each line