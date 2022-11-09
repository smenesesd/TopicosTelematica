from mrjob.job import MRJob

class mapReduce(MRJob):

    def mapper(self, _, line):
        company, price, date = line.split(',')
        lista = [date, float(price)]
        yield company, lista

    def reducer(self, company, values):
        l = list(values)
        exito = False
        price = l[0][1]
        for n in l:
            if n[1] > price:
                price = price
                exito = True
            else:
                exito = False
        yield company, exito 

if __name__ == '__main__':
    mapReduce.run()