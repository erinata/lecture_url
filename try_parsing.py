from bs4 import BeautifulSoup

f = open("sample.html", "r")

# print(f.read())

soup = BeautifulSoup(f.read(), 'html.parser')

#print(soup.td)

# results = soup.find_all('td')
# # print(results)

# for r in results:
# 	print(r.text)

# results = soup.find('table').children

# for r in results:
# 	print(r)


results = soup.find_all('tr')

for r in results:
	for c in r.children:
		print(c)
		
















