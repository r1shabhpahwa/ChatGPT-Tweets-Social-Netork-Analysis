import csv

# # continents = {
# #     'Asia': ['China', 'India', 'Indonesia', 'Pakistan', 'Bangladesh', 'Japan', 'Philippines', 'Vietnam', 'Iran', 'Turkey'],
# #     'Africa': ['Nigeria', 'Ethiopia', 'Egypt', 'DR Congo', 'Tanzania', 'South Africa', 'Kenya', 'Uganda', 'Algeria', 'Sudan'],
# #     'North America': ['United States', 'Canada', 'Mexico'],
# #     'South America': ['Brazil', 'Colombia', 'Argentina', 'Peru', 'Venezuela', 'Chile', 'Ecuador', 'Bolivia', 'Paraguay', 'Uruguay'],
# #     'Europe': ['Russia', 'Germany', 'United Kingdom', 'France', 'Italy', 'Spain', 'Ukraine', 'Poland', 'Romania', 'Netherlands'],
# #     'Oceania': ['Australia', 'Papua New Guinea', 'New Zealand']
# # }


continents = {
    'Asia': ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia', 'China', 'Cyprus', 'Georgia', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar (Burma)', 'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Russia', 'Saudi Arabia', 'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'Timor-Leste (East Timor)', 'Turkey', 'Turkmenistan', 'United Arab Emirates (UAE)', 'Uzbekistan', 'Vietnam', 'Yemen'],
    'Africa': ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cameroon', 'Central African Republic (CAR)', 'Chad', 'Comoros', 'Democratic Republic of the Congo', 'Republic of the Congo', 'Cote d\'Ivoire', 'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini (formerly Swaziland)', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe'],
    'Europe': ['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kazakhstan', 'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia (formerly Macedonia)', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom (UK)', 'Vatican City (Holy See)'],
    'North America': ['Antigua and Barbuda', 'Bahamas', 'Barbados', 'Belize', 'Canada', 'Costa Rica', 'Cuba'],
    'South America':['Argentina','Bolivia','Brazil','Chile','Colombia','Ecuador','Guyana','Paraguay','Peru','Suriname','Uruguay','Venezuela'],
    'Oceania':['Fiji','Kiribati','Marshall Islands', 'Micronesia','Nauru','New Zealand','Palau','Palau','Papua New Guinea','Samoa','Solomon Islands','Tonga','Tuvalu','Vanuatu']
    }

continents_files = {continent: open(f'{continent}.csv', 'w', newline='', encoding='utf-8') for continent in continents}
missing_file = open('missing.csv', 'w', newline='', encoding='utf-8')

csvwriter_dict = {}
for continent, file in continents_files.items():
    csvwriter_dict[continent] = csv.DictWriter(file, fieldnames=['Date', 'Tweet', 'City', 'Country'])
    csvwriter_dict[continent].writeheader()

csvwriter_missing = csv.DictWriter(missing_file, fieldnames=['Date', 'Tweet', 'City', 'Country'])
csvwriter_missing.writeheader()

with open('output.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        try:
            date, city, country = row['Date'], row['City'], row['Country']
            continent = None
            for cont, countries in continents.items():
                if country in countries:
                    continent = cont
                    break
            if continent is None:
                raise ValueError(f'No continent found for country {country}')
            csvwriter_dict[continent].writerow({'Date': date, 'Tweet': row['Tweet'], 'City': city, 'Country': country})
        except (KeyError, ValueError):
            csvwriter_missing.writerow({'Date': row.get('Date', 'N/A'), 'Tweet': row['Tweet'], 'City': row.get('City', 'N/A'), 'Country': row.get('Country', 'N/A')})

for file in continents_files.values():
    file.close()

missing_file.close()

# import csv

# continents = {
#     'Asia': ['China', 'India', 'Indonesia', 'Pakistan', 'Bangladesh', 'Japan', 'Philippines', 'Vietnam', 'Iran', 'Turkey'],
#     'Africa': ['Nigeria', 'Ethiopia', 'Egypt', 'DR Congo', 'Tanzania', 'South Africa', 'Kenya', 'Uganda', 'Algeria', 'Sudan'],
#     'North America': ['United States', 'Canada', 'Mexico'],
#     'South America': ['Brazil', 'Colombia', 'Argentina', 'Peru', 'Venezuela', 'Chile', 'Ecuador', 'Bolivia', 'Paraguay', 'Uruguay'],
#     'Europe': ['Russia', 'Germany', 'United Kingdom', 'France', 'Italy', 'Spain', 'Ukraine', 'Poland', 'Romania', 'Netherlands'],
#     'Oceania': ['Australia', 'Papua New Guinea', 'New Zealand']
# }


# continents = {
#     'Asia': ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia', 'China', 'Cyprus', 'Georgia', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar (Burma)', 'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Russia', 'Saudi Arabia', 'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'Timor-Leste (East Timor)', 'Turkey', 'Turkmenistan', 'United Arab Emirates (UAE)', 'Uzbekistan', 'Vietnam', 'Yemen'],
#     'Africa': ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cameroon', 'Central African Republic (CAR)', 'Chad', 'Comoros', 'Democratic Republic of the Congo', 'Republic of the Congo', 'Cote d\'Ivoire', 'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini (formerly Swaziland)', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe'],
#     'Europe': ['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kazakhstan', 'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia (formerly Macedonia)', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom (UK)', 'Vatican City (Holy See)'],
#     'North America': ['Antigua and Barbuda', 'Bahamas', 'Barbados', 'Belize', 'Canada', 'Costa Rica', 'Cuba'],
#     'South America':['Argentina','Bolivia','Brazil','Chile','Colombia','Ecuador','Guyana','Paraguay','Peru','Suriname','Uruguay','Venezuela'],
#     'Oceania':['Fiji','Kiribati','Marshall Islands', 'Micronesia','Nauru','New Zealand','Palau','Palau','Papua New Guinea','Samoa','Solomon Islands','Tonga','Tuvalu','Vanuatu']
#     }

# continents_files = {continent: open(f'{continent}.csv', 'w', newline='', encoding='utf-8') for continent in continents}
# missing_file = open('missing.csv', 'w', newline='', encoding='utf-8')

# csvwriter_dict = {}
# for continent, file in continents_files.items():
#     csvwriter_dict[continent] = csv.DictWriter(file, fieldnames=['Date','Tweet', 'City', 'Country'])
#     csvwriter_dict[continent].writeheader()

# csvwriter_missing = csv.DictWriter(missing_file, fieldnames=['Date','Tweet', 'City', 'Country'])
# csvwriter_missing.writeheader()

# with open('output.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.DictReader(csvfile)
#     for row in csvreader:
#         try:
#             city, country = row['City'], row['Country']
#             continent = None
#             for cont, countries in continents.items():
#                 if country in countries:
#                     continent = cont
#                     break
#             if continent is None:
#                 raise ValueError(f'No continent found for country {country}')
#             csvwriter_dict[continent].writerow({'Date': row['date'],'Tweet': row['Tweet'], 'City': city, 'Country': country})
#         except (KeyError, ValueError):
#             csvwriter_missing.writerow({'Date': row['date'],'Tweet': row['Tweet'], 'City': row.get('City', 'N/A'), 'Country': row.get('Country', 'N/A')})

# for file in continents_files.values():
#     file.close()

# missing_file.close()