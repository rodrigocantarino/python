""""

Writing CSV Files



"""
from csv import writer, DictWriter

"""
# Writer -> from csv import writer
with open('movies.csv', 'a') as file:
    csv_writer = writer(file)
    movie = None
    csv_writer.writerow(['Title', 'Genre', 'Runtime', 'Year'])
    while movie != 'exit':
        print('--------------------------------------------------------')
        movie = input('Movie name: ')
        if movie != 'exit':
            genre = input('Movie Genre: ')
            runtime = input('Movie Runtime: ')
            year = input('Movie Year: ')
            csv_writer.writerow([movie, genre, runtime, year])

"""

# DictWriter -> from csv import DictWriter
with open('movies2.csv', 'a') as file:
    header = ['Title', 'Genre', 'Runtime', 'Year']
    csv_writer = DictWriter(file, fieldnames=header)
    csv_writer.writeheader()
    movie = None
    while movie != 'exit':
        print('--------------------------------------------------------')
        movie = input('Movie name: ')
        if movie != 'exit':
            genre = input('Movie Genre: ')
            runtime = input('Movie Runtime: ')
            year = input('Movie Year: ')
            # The dictionary keys must be the same as the HEADER
            csv_writer.writerow({'Title': movie, 'Genre': genre, 'Runtime': runtime, 'Year': year})
