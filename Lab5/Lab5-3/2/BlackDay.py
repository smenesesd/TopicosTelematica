from mrjob.job import MRJob



class mapReduce(MRJob):
    global precioBlackDay
    global fechaBlackDay
    precioBlackDay = 0
    fechaBlackDay = ""

    def mapper(self, _, line):
        company, price, date = line.split(',')
        yield company, price

    def reducer(self, date, values):
        mayor = precioBlackDay
        l = list(values)

        if precioBlackDay < sum(l):
            precioBlackDay = sum(l)
            fechaBlackDay = date
            


if __name__ == '__main__':
    mapReduce.run()
    print("precio BlackDay: ", fechaBlackDay)