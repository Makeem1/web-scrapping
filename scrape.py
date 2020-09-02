import requests
from bs4 import BeautifulSoup
import pprint
 
res = requests.get("https://news.ycombinator.com/")  # This is the url, store in res variable

res_string = res.text

soup = BeautifulSoup(res_string, "html.parser")
links = soup.select(".storylink")
# votes = soup.select(".score")
subtext = soup.select(".subtext")

def sort_hn_list(hnlist):
	return sorted(hnlist, key=lambda k:k["votes"], reverse=True)

def custom_create_hn(links, subtext):
	hn = []
	for idx, item in enumerate(links):
		title = item.get_text() 
		href = item.get("href", None)
		votes = subtext[idx].select(".score")
		if len(votes): 
			points = int(votes[0].get_text().replace(" points", ''))
			if points > 100:
				hn.append({"title":title, "link":href, "votes": points})
	return sort_hn_list(hn)

pprint.pprint(custom_create_hn(links,subtext))






# print(soup.prettify())   ''' this help to print the html page in a structured format '''
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.find_all("a"))

# for link in soup.find_all('a'):
# 	print(link.get("href"))

# print(soup.get_text())
