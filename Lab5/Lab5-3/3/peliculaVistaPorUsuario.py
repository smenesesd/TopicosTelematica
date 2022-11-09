from mrjob.job import MRJob

class mapReduce(MRJob):

    def mapper(self, _, line):
        user, movie,rating,genre,date = line.split(',')
        lista = [movie, float(rating)]
        yield user, lista

    def reducer(self, user, values):
        l = list(values)
        avg = 0
        for i in l:
            avg += i[1]
        avg = avg / len(l)

        yield user, (len(l), avg)

if __name__ == '__main__':
    mapReduce.run()