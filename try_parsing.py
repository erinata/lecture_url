from bs4 import BeautifulSoup

f = open("sample.html", "r")

# print(f.read())

soup = BeautifulSoup(f.read(), 'html.parser')

#print(soup.td)

results = soup.find_all('td')
# print(results)

for r in results:
	print(r.text)

	







