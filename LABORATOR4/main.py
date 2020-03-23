from random import seed

from GA import GA
from Repository import Repository
from UI import UI


def main():
    #seed(1)
    repository = Repository("E:\\ANUL II\\SEMESTRUL II\\INTELIGENTA ARTIFICIALA\\LABORATOR4\\resources\\easy_01_tsp.txt")
    params = {'popSize': 5, 'noGen': 100}
    ga = GA(params, repository.params)
    ui = UI(ga)
    ui.run()

main()