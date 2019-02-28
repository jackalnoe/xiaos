from requests_html import HTMLSession


def get_one_page(all_url):
	url = 'https://www.biqukan.com/0_104/24099.html'
	session = HTMLSession()
	res = session.get(url)
	targets = res.html.find('#content')
	content = targets[0].text
	print(content)

first_url = 'https://www.biqukan.com'
target_url = 'https://www.biqukan.com/0_104/'
session = HTMLSession()
res = session.get(target_url)
targets = res.html.find('.listmain dd')
titles = []
hrefs = []
for i in range(12, len(targets)):
	titles.append(targets[i].text) 
	hrefs.extend(list(targets[i].links))
	print(titles)
	print(hrefs)
