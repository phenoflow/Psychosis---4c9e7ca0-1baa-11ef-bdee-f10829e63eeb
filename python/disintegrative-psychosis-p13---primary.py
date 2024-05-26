# S Jill Stocks, Evangelos Kontopantelis, Roger T Webb, Anthony J Avery, Alistair Burns, Darren M Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"Eu10500","system":"readv2"},{"code":"Eu19700","system":"readv2"},{"code":"Eu18400","system":"readv2"},{"code":"Eu18500","system":"readv2"},{"code":"Eu12700","system":"readv2"},{"code":"Eu15700","system":"readv2"},{"code":"Eu11400","system":"readv2"},{"code":"Eu19400","system":"readv2"},{"code":"Eu14500","system":"readv2"},{"code":"Eu12500","system":"readv2"},{"code":"Eu13400","system":"readv2"},{"code":"E141100","system":"readv2"},{"code":"Eu13500","system":"readv2"},{"code":"Eu11700","system":"readv2"},{"code":"Eu16500","system":"readv2"},{"code":"Eu10700","system":"readv2"},{"code":"Eu11500","system":"readv2"},{"code":"Eu10400","system":"readv2"},{"code":"Eu15500","system":"readv2"},{"code":"E141.00","system":"readv2"},{"code":"Eu14700","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('psychosis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["disintegrative-psychosis-p13---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["disintegrative-psychosis-p13---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["disintegrative-psychosis-p13---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
