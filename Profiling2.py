from memory_profiler import profile

@profile
def quadrados():
    return [i**2 for i in range (10_000_000)]

@profile
def cubos():
    return [i**3 for i in range (10_000_000)]

@profile
def main():
    quadrados()
    cubos()

main()