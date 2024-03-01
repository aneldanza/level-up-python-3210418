import csv

def merge_csv(csv_list, ouptut_path):
  header = set()
  dict_list = []
  
  for file in csv_list:
    with open(file, mode='r') as f:
      dict = csv.DictReader(f)
      rows = []

      for row in dict:
        rows.append(row)

      dict_list.append(rows)
      header = header.union(rows[0].keys())
  
    
    with open(ouptut_path, mode='w') as o:
      writer = csv.DictWriter(o, fieldnames=header)
      writer.writeheader()
      
      for file in dict_list:
        for row in file:
          writer.writerow(row)

merge_csv(['class1.csv', 'class2.csv'], 'all_students.csv')