import os, csv, glob

dupe_docs = glob.glob(f'duplicates/*.csv')
dupe_originals = []
dupe_paths = []
for doc in dupe_docs:
    with open(doc) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            dupe_originals.append(row[0])
            dupe_paths.append(row[1])
            
for path in set(dupe_paths):
  try:
    os.remove(path)
  except FileNotFoundError:
    print(f'{path} not found')