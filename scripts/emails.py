with open("./inputs/emails.csv", 'r') as file:
    reader = csv.reader(file.readlines())

with open('emails_solution.csv', 'w') as outf:
    writer = csv.writer(outf)
    for line in reader:
        temp_line = line
        temp_line[1] = re.sub("@[a-z0-9.-]+(.)?[a-z]{2,4}", "@mlh.io", line[1])
        writer.writerow(temp_line)
    writer.writerows(reader)
