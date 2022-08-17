email_file = open("../inputs/emails.csv", "r")
email_reader = csv.reader(email_file)

out_file = open("emails_new.csv", "w")
out_writer = csv.writer(out_file)
for row in email_reader:
    email = row[1]
    row[1] = re.sub("@gmail\.com", "@mlh.io", row[1])
    out_writer.writerow(row)

email_file.close()
out_file.close()
