from mrjob.job import MRJob

class mapReduce(MRJob):

    def mapper(self, _, line):
        user, movie,rating,genre,date = line.split(',')
        lista = [user, float(rating)]
        yield movie, lista

    def reducer(self, movie, values):
        l = list(values)
        avg = 0
        for i in l:
            avg += i[1]

        yield movie, (len(l), avg/len(l))

if __name__ == '__main__':
    mapReduce.run()