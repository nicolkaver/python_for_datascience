import csv
import matplotlib.pyplot as plt

def convert_to_number(string: str):
    multipliers = {'k': 10 ** 3, 'M': 10 ** 6, 'G': 10 ** 9, 'T': 10 ** 12}  # Add more if needed
    suffix = string[-1]

    if suffix.isdigit():
        return int(string)
    elif suffix in multipliers:
        numeric_part = float(string[:-1])
        return int(numeric_part * multipliers[suffix])
    else:
        raise ValueError("Invalid suffix")

def load(path: str, country_name: str, other_country: str):
    try:
        with open(path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            header = next(csv_reader)
            num_columns = len(header)
            num_rows = 0
            data = []
            years = header[1:]
            selected_years = [1800, 1840, 1880, 1920, 1960, 2000, 2040] 
            population1 = None
            population2 = None
            first_time_looping = True
            for row in csv_reader:
                num_rows += 1
                data.append(row)
                if first_time_looping == True:
                    print(f"Loading datasest of dimensions {num_columns, num_rows}")
                    print(' '.join(header[:5]) + " ... " + ' '.join(header[-5:]))
                    print(' '.join(data[0][:5]) + " ... " + ' '.join(data[0][-5:]))
                    print("...")
                    first_time_looping = False
                if row[0] == country_name:
                    population1 = [convert_to_number(pop) for pop in row[1:]]
                elif row[0] == other_country:
                    population2 = [convert_to_number(pop) for pop in row[1:]]
                    break
            if population1 is None or population2 is None:
                print(f"No data found for {country_name} or {other_country}")
                return

            plt.figure(figsize=(10, 6))
            plt.plot(years, population1, marker='o', label=f"{country_name}")
            plt.plot(years, population2, marker='o', label=f"{other_country}")
            plt.title(f"Population of {country_name} and {other_country} over the years")
            plt.xlabel('Year')
            plt.ylabel('Population')
            plt.grid(False)
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.legend()
            plt.show()

    except FileNotFoundError:
        print("Invalid path")
        return None
    except csv.Error as e:
        print(f"CSV file error: {e}")
    