from math import factorial, comb, pow, e
from random import randint

class Bernoulli:
    def __init__(self, probability: float) -> None:
        self.p = probability
    
    def density_function(self, x: int):
        return pow(self.p, x) * pow(1 - self.p, 1 - x)
    
    def mean(self):
        return self.p

    def variance(self):
        return self.p * (1 - self.p)
    
class Binomial:
    def __init__(self, probability: float, experiment_number: int) -> None:
        self.p = probability
        self.n = experiment_number
    
    def density_function(self, k: int):
        return comb(self.n, k) * pow(self.p, k) * pow(1 - self.p, self.n - k)
    
    def mean(self):
        return self.n * self.p
    
    def variance(self):
        return self.mean() * (1 - self.p)

class Geometric:
    def __init__(self, probability: float, success_number: int) -> None:
        self.p = probability
        self.x = success_number
        
    def density_function(self):
        return self.p * pow(1 - self.p, self.x - 1)
    
    def mean(self):
        return 1 / self.p
    
    def variance(self):
        return (1 - self.p) / pow(self.p, 2)

class Poisson:
    def __init__(self, ocurrencies_number: int, lamb: float) -> None:
        self.k = ocurrencies_number
        self.lamb = lamb
        
    def density_function(self):
        return (pow(e, -self.lamb) * pow(self.lamb, self.k)) / factorial(self.k)
    
    def mean(self):
        return self.lamb
    
    def variance(self):
        return self.lamb

if __name__ == "__main__":
    base_probability = 1/6
    # Definición de Bernoulli
    SUCESS = 1
    FAIL = 0
    bernoulli = Bernoulli(probability=base_probability)
    
    # Definición Binomial
    n = 10
    success_experiment = randint(0, n)
    binomial = Binomial(probability=base_probability, experiment_number=10)
    
    # Definicion Geométrica
    success_index = 4
    geometric = Geometric(probability=base_probability, success_number=success_index)
    
    # Definición de Poisson
    ocur_num = 5
    mean = 6
    minutes = 10
    time_interval = minutes * mean
    poisson = Poisson(ocurrencies_number=ocur_num, lamb=time_interval)
    
    print(f"Probabilidad base: {base_probability}")
    print(f"============================================")
    print(f"Función de densidad de Bernoulli con éxitos: {bernoulli.density_function(SUCESS)}")
    print(f"Función de densidad de Bernoulli con fallos: {bernoulli.density_function(FAIL)}")
    print(f"Media de Bernoulli: {bernoulli.mean()}")
    print(f"Varianza de Bernoulli: {bernoulli.variance()}")
    print(f"============================================")
    print(f"Función de densidad binomial con {success_experiment} éxitos: {binomial.density_function(success_experiment)}")
    print(f"Media Binomial: {binomial.mean()}")
    print(f"Varianza Binomial: {binomial.variance()}")
    print(f"============================================")
    print(f"Función de densidad geométrica con {success_index} intentos: {geometric.density_function()}")
    print(f"Media Geomética: {geometric.mean()}")
    print(f"Varianza Geomética: {geometric.variance()}")
    print(f"============================================")
    print(f"Función de densidad de Poisson con {ocur_num} ocurrencias en {minutes} minutos: {poisson.density_function()}")
    print(f"Media de Poisson: {poisson.mean()}")
    print(f"Varianza de Poisson: {poisson.variance()}")