import statistics
from read_csv import get_file, get_formated_data

def media(data):
    return statistics.mean(data)

def mediana(data):
    return statistics.median(data)

def moda(data):
    return statistics.mode(data)

def cuantil(data, region):
    return statistics.quantiles(data, n= region)

def rango(data):
    return abs(max(data) - min(data))

if __name__ == "__main__":
    file = get_file("descriptive/data.csv")
    ages = get_formated_data(file)
    
    print(f"Media: {media(ages)}")
    print(f"Mediana: {mediana(ages)}")
    print(f"Moda: {moda(ages)}")
    print(f"Rango: {rango(ages)}")
    print(f"Cuantil (4 regiones): {cuantil(ages, 4)}")