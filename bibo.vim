import requests
from ebooklib import epub
from bs4 import BeautifulSoup

#get the html file using requests
content = requests.get('http://paulgraham.com/articles.html')
book = epub.EpubBook()
book.set_identifier('PGsample0')
book.set_title('Sample book')
book.set_language('en')
book.add_author('Paul Graham')

#making the soup 
soup = BeautifulSoup(content.content, 'html.parser')

#get the table of articles and get the rows  
table = soup.table
table_rows = table.find_all('tr')
td = soup.find_all('td')
links = []
for t in td:
	query = t.find('a')
	if query != None:
		links.append(query)

for link in links[:4]:
	print(f'Downloading {link.text}')
	article = requests.get(f"http://paulgraham.com/{link.get('href')}")
	article_soup = BeautifulSoup(article.content , 'html.parser')
	chapter = epub.EpubHtml(title = link.text , file_name = f'{link.text}.xhtml' , 
				lang = 'en')
	chapter.set_content(link.font)
	book.add_item(chapter)
	book.toc.append(chapter)
	book.spine.append(chapter)



style= 'BODY {color:white;}'
nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css"
                        , media_type="text/css",content=style)

book.add_item(nav_css)
book.spine.append('nav')



epub.write_epub('pgtest.epub' , book)

