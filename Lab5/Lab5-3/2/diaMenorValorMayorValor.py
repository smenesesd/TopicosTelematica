from mrjob.job import MRJob

class mapReduce(MRJob):

    def mapper(self, _, line):
        company, price, date = line.split(',')
        lista = [float(price), date]
        yield company, lista

    def reducer(self, company, values):
        l = list(values)
        mayor = 0
        mayorDat = ""
        menor = 100000000000000
        menorDat = ""
        for i in l:
            if i[0] > mayor:
                if mayor != 0 and mayor < menor:
                    menorDat = mayorDat
                    menor = mayor
                mayorDat = i[1]
                mayor = i[0]
            if i[0] < menor:
                menor = i[0]
                menorDat = i[1]



        yield company, (menorDat, mayorDat)

if __name__ == '__main__':
    mapReduce.run()