import csv
import os

# def check_file_path(path: str):
#     if os.path.exists(path):
#         return True
#     else:
#         return False

def load(path: str):
    try:
        # assert check_file_path(path) == True, "Invalid path"
        with open(path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            header = next(csv_reader)
            num_columns = len(header)
            num_rows = 0
            data = []
            for row in csv_reader:
                num_rows += 1
                data.append(row)
            print(f"Loading datasest of dimensions {num_columns, num_rows}")
            print(' '.join(header[:5]) + " ... " + ' '.join(header[-5:]))
            print(' '.join(data[0][:5]) + " ... " + ' '.join(data[0][-5:]))
    # except AssertionError as e:
    #     print(f"{type(e).__name__} : {e}")
    #     return None
    except FileNotFoundError:
        print("Invalid path")
        return None
    except csv.Error as e:
        print(f"CSV file error: {e}")
    