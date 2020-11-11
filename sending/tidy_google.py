import csv
import glob
import re

regex = re.compile(r"[0-9]{4}")
csvfiles = glob.glob("*.csv")

for csvfile in csvfiles:
    with open(csvfile) as csvfile:
        csv_object = csv.reader(csvfile)
        for row in csv_object:
            mobile = None

            for column in row:
                if regex.search(column):
                    mobile = column
                    break

            if mobile:
                mobile_ar = [str(int(char)) for char in mobile if char.isdigit()]
                mobile = ''.join(mobile_ar)

                if mobile.startswith("9"):
                    mobile = "71" + mobile

                if not mobile.startswith("71"):
                    continue

                if len(mobile) == 10 and mobile.startswith("719"):
                    mobile = "7199" + mobile[3:]

                if not mobile.startswith("719") or not len(mobile) == 11:
                    continue

                print(mobile)
