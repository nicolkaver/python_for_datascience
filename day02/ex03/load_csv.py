import csv
import matplotlib.pyplot as plt
from sympy import Q

def print_file_info(header: list[str], data: list, num_columns: int, num_rows: int):
    print(f"Loading datasest of dimensions {num_columns, num_rows}")
    print(' '.join(header[:5]) + " ... " + ' '.join(header[-5:]))
    print(' '.join(data[0][:5]) + " ... " + ' '.join(data[0][-5:]))
    print("...")

def load(path1: str, path2: str):
    try:
        countries_to_plot = []
        life_expectancy_data = {}
        with open(path1, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            header = next(csv_reader)
            # index1900 = row[header.index("1900")] if "1900" in header else None
            # for index, value in enumerate(header):
            #     if value == "1900":
            #         index1900 = index
            num_columns = len(header)
            num_rows = 0
            data = []
            first_time_looping = True
            for row in csv_reader:
                num_rows += 1
                data.append(row)
                country = row[0]
                countries_to_plot.append(country)
                if first_time_looping == True:
                    print_file_info(header, data, num_columns, num_rows)
                    first_time_looping = False
                # for i in row:
                #     if i == index1900:
                #         life_expectancy_data[country] = row[i]
                #         print(country)
                life_expectancy_1900 = row[header.index("1900")] if "1900" in header else None
                if life_expectancy_1900 is not None:
                    if len(life_expectancy_1900) == 0:
                        life_expectancy_data[country] = 0.
                    else:
                        life_expectancy_data[country] = float(life_expectancy_1900)

        gdp_data = {}
        with open(path2, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            header = next(csv_reader)
            index1900 = 0
            for index, value in enumerate(header):
                if value == "1900":
                    index1900 = index
            num_columns = len(header)
            num_rows = 0
            data = []
            first_time_looping = True
            for row in csv_reader:
                num_rows += 1
                data.append(row)
                country = row[0]
                if first_time_looping == True:
                    print_file_info(header, data, num_columns, num_rows)
                    first_time_looping = False
                # for i in row:
                #     if i == index1900:
                #         gdp_data[country] = row[i]
                gdp_1900 = row[header.index("1900")] if "1900" in header else None
                if gdp_1900 is not None:
                    gdp_data[country] = float(gdp_1900)

        plt.figure(figsize=(10, 6))
        for country in countries_to_plot:
            plt.plot(gdp_data[country], life_expectancy_data[country], marker='o', label=country)
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life expectancy")
        plt.grid(False)
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print("Invalid path")
        return None
    except csv.Error as e:
        print(f"CSV file error: {e}")
    