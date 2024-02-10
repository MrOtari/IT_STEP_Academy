############# Question 1

import csv

with open("titanic.csv", "r") as titanic:
    csv_reader = csv.DictReader(titanic)

    with open("survived.csv", "w", newline="") as survived:
        header = ["Survived"]
        csv_writer = csv.DictWriter(survived, fieldnames=header)
        csv_writer.writeheader()

        for i in csv_reader:
            csv_writer.writerow({"Survived": i["Survived"]})



############# Question 2

with open("organizations-100.csv", "r") as org:
   org_reader = csv.reader(org)
   header = next(org_reader)
   sorted_org_reader = sorted(org_reader, key=lambda i: int(i[-1]))
   sorted_org_reader.insert(0, header)

with open("sorted_csv.csv", "w", newline="") as comp:
   org_writer = csv.writer(comp)
   org_writer.writerows(sorted_org_reader)



############# Question 3

import csv

with open("organizations-100.csv", "r") as org:
   org_reader = csv.DictReader(org) 
   lst = []
   for rows in org_reader:
      if rows["Website"].startswith("https") :
         lst.append(rows)

with open("ssl_companies.csv", "w", newline="") as comp:
   header = ["Organization Id","Name","Website","Industry","Number of employees"]
   writer = csv.DictWriter(comp, fieldnames=header)

   writer.writeheader()
   for i in lst:
      del i["Index"]
      del i["Country"]
      del i["Founded"]
      del i["Description"]
   writer.writerows(lst)