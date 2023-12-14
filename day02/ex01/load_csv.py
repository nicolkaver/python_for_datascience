import csv
import matplotlib.pyplot as plt

def load(path: str, country_name: str):
    try:
        with open(path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            header = next(csv_reader)
            years = header[1:]
            life_expectancy = None
            num_columns = len(header)
            num_rows = 0
            data = []
            for row in csv_reader:
                num_rows += 1
                data.append(row)
                if row[0] == country_name:
                    life_expectancy = row[1:]
            print(f"Loading datasest of dimensions {num_columns, num_rows}")
            print(' '.join(header[:5]) + " ... " + ' '.join(header[-5:]))
            print(' '.join(data[0][:5]) + " ... " + ' '.join(data[0][-5:]))
    
            plt.figure(figsize=(10, 6))
            plt.plot(years, life_expectancy, marker='o')
            plt.title(f"{country_name} Life expectancy Projection")
            plt.xlabel('Year')
            plt.ylabel('Life expectancy')
            plt.grid(False)
            plt.xticks(range(0, 300, 40), rotation=45)
            plt.tight_layout()
            plt.show()
    except FileNotFoundError:
        print("Invalid path")
        return None
    except csv.Error as e:
        print(f"CSV file error: {e}")
    