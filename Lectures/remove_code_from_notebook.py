import json
import sys

file_path = ""
file_path_after = ""
nb_file = ""

if __name__ == "__main__":
    # Argument Debug
    # print(f"Arguments count: {len(sys.argv)}")
    # for i, arg in enumerate(sys.argv):
    #     print(f'Argument {i:>6}: {arg}')

    if len(sys.argv) < 2:
        print("Usage: python remove_code_from_Notebook.py <Notebook.ipynb> (overwrites Notebook.ipynb)")
        print("Usage: python remove_code_from_Notebook.py <Notebook.ipynb> <Notebook_after.ipynb>")
        sys.exit(1)

    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        print(f"Reading Notebook file: {file_path}")
        nb_file = open(file_path, "r")  # change this to your file path

    if len(sys.argv) == 3:
        file_path = sys.argv[1]
        file_path_after = sys.argv[2]
        print(f"Reading Notebook file: {file_path}")
        nb_file = open(file_path, "r")

    if len(sys.argv) > 3:
        print("Usage: python remove_code_from_Notebook.py <Notebook.ipynb> (overwrites Notebook.ipynb)")
        print("Usage: python remove_code_from_Notebook.py <Notebook.ipynb> <Notebook_after.ipynb>")
        sys.exit(1)

    nb_file = open(file_path, "r")
    notebook = json.load(nb_file)  # Loads a ipynb file
    nb_file.close()

    for cell in notebook["cells"]:
        if cell["cell_type"] == "code":
            cell["source"] = []  # removes all the code

    with open(file_path_after, "w") as f:
        json.dump(notebook, f, indent=2)
