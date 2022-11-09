from mrjob.job import MRJob

class mapReduce(MRJob):

    def mapper(self, _, line):
        idemp, sector,salary,year = line.split(',')
        yield idemp, int(sector)

    def reducer(self, idemp, values):
        lista_sectores = list(values)
        lista_no_repetida = []
        for i in lista_sectores:
            if i not in lista_no_repetida: 
                lista_no_repetida.append(i)
        yield idemp, len(lista_no_repetida)

if __name__ == '__main__':
    mapReduce.run()