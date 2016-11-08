from bs4 import BeautifulSoup
import requests

id_list = {}
url = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2015/office_id:1/stage:General"
y  = requests.get(url)
data = y.text

soup = BeautifulSoup(data, "html.parser")
rows = soup.find_all("tr")

with open("ELECTION_ID", "w") as out:
    for row in rows:
        #print (row)                      # get content in this row
        id = str(row.get("id"))           # get id of this row
        begin = id.find("election-id-")   # see if id starts with "election-id-"
        if (begin != -1):
            election_id  = id[12:]        # skip the leading characters
            cell = row.find("td")         # the first cell contains the "election year"
            year = cell.string
            a = year + " " + election_id + "\n"
            out.write(a)
for line in open("ELECTION_ID"):
    print(line)
