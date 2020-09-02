import re
import csv
import requests
from urllib import robotparser
from urllib.request import urlopen, urljoin, urlparse
from bs4 import BeautifulSoup, SoupStrainer



website = 'http://www.nairaland.com/'


# def format_for_robot_text(website):
# 	robot_text = '/robots.txt'
# 	if website.endswith('/'):
# 		robot_text = website + robot_text[1:]
# 	else:
# 		robot_text = website + robot_text
# 	return robot_text


# robot_parser = robotparser.RobotFileParser()

# # Check if website is Crawlable
# def prepare(robots_txt_url):
# 	robot_parser.set_url(robots_txt_url)
# 	robot_parser.read()


# def is_allowed(target_url, user_agent='*'):
# 	return robot_parser.can_fetch(user_agent, target_url)
# # print(is_allowed(format_for_robot_text(website)))


def download_page(url):
	return requests.get(url).text



def extract_links(page):
	if not page:
		return []
	link_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
	return [urljoin(page, link) for link in link_regex.findall(page)]


def get_links(page_url):
	host = urlparse(page_url)[1]
	page = download_page(page_url)
	links = extract_links(page)
	return [link for link in links if urlparse(link)[1] == host]


# print(get_links(website))
def get_page(url):
	try:
		r = requests.get(url)
		if r.status_code == 200:
			strainer = SoupStrainer(name='table', attrs={'summary':'posts'})
			return BeautifulSoup(r.content, 'html.parser',  parse_only=strainer)
	except Exception as e:
		print(e)
	return None

def map_urljoin(website, user):
	return "".join(website, user['href'])




def custom_crawler(start_url):
	from collections import deque
	
	visited = set()
	stack = deque()
	# stack.append(start_url)
	stack.extend(get_links(start_url))
	while stack:
		url = stack.popleft()
		if url in visited:
			continue
		visited.add(url)
		soup = get_page(url)	#BS
		# url_links = get_links(url)
		# thrend = soup #soup.find('table', attrs={'summary':'posts'})
		if not soup:
			continue
		users = soup.find_all('a', attrs={'class':'user'})
		# for user in users:
		print(list(map(lambda user: urljoin(website, user['href']), users)))
custom_crawler(website)