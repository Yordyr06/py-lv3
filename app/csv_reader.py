import csv

def read_csv(path):
  with open(path, 'r') as file:
    reader = csv.reader(file, delimiter = ',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      data.append(dict(iterable))
    return data

if __name__ == '__main__':
  data = read_csv('data.csv')
  print(data[0])