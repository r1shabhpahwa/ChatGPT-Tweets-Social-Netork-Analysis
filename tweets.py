# import csv

# # Input and output file paths
# input_file = 'ChatGPT.csv'
# output_file = 'output.csv'

# # Read the input file and extract the required columns
# rows = []
# with open(input_file, 'r', encoding='utf-8') as f:
#     csvreader = csv.DictReader(f)
#     for row in csvreader:
#         try:
#             city, country = row['Location'].split(',')
#             rows.append({
#                 'Tweet': row['Tweet'],
#                 'City': city.strip(),
#                 'Country': country.strip()
#             })
#         except ValueError:
#             pass

# # Write the extracted data to the output file
# with open(output_file, 'w', newline='', encoding='utf-8') as f:
#     fieldnames = ['Tweet', 'City', 'Country']
#     csvwriter = csv.DictWriter(f, fieldnames=fieldnames)
#     csvwriter.writeheader()
#     for row in rows:
#         csvwriter.writerow(row)


import csv

# Input and output file paths
input_file = 'ChatGPT.csv'
output_file = 'output.csv'

# Read the input file and extract the required columns
rows = []
with open(input_file, 'r', encoding='utf-8') as f:
    csvreader = csv.DictReader(f)
    for row in csvreader:
        try:
            date = row['Date']
            city, country = row['Location'].split(',')
            rows.append({
                'Date': date,
                'Tweet': row['Tweet'],
                'City': city.strip(),
                'Country': country.strip()
            })
        except (ValueError, KeyError):
            pass

# Write the extracted data to the output file
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['Date', 'Tweet', 'City', 'Country']
    csvwriter = csv.DictWriter(f, fieldnames=fieldnames)
    csvwriter.writeheader()
    for row in rows:
        csvwriter.writerow(row)