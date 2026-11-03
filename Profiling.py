#Analisar o desempenho de um programa enquanto ele está em execução
#cProfile - padrão: mede tempo de execução
#memory_profile - acompanha consumo de memória durante a execução
import cProfile
def quadrados():
    return [i**2 for i in range (100_000_000)]

def cubos():
    return [i**3 for i in range (100_000_000)]

def main():
    quadrados()
    cubos()

cProfile.run("main()")