import requests
from ebooklib import epub
from bs4 import BeautifulSoup

#initialize e-book META data.
book = epub.EpubBook()
book.set_identifier('PGsample0')
book.set_title('PG articles e-book')
book.set_language('en')
book.add_author('Paul Graham')


def scrape_articles(url):
    #get HTML file using requests & BeautifulSoup
    content = requests.get(url)
    soup = BeautifulSoup(content.content, 'html.parser')

    table = soup.table
    table_rows = table.find_all('tr')
    td = soup.find_all('td')
    links = []
    for t in td:
	    query = t.find('a')
	    if query != None:
	        links.append(query)
    create_ebook(links)

'''
style = 'body { font-family: Times, Times New Roman, serif; }'

nav_css = epub.EpubItem(uid="style_nav",
                                                file_name="style/nav.css",
                                                media_type="text/css",
                                                content=style)
book.add_item(nav_css)
'''
def create_ebook(links):
    # remove the first and last element
    links.remove(links[0])
    links.remove(links[-1])
    for link in links:
        print(f'Downloading {link.text}')
        article = requests.get(f"http://paulgraham.com/{link.get('href')}")
        article_soup = BeautifulSoup(article.content , 'html.parser')
        chapter = epub.EpubHtml(title = str(link.text) ,
                         file_name = f'{link.text}.xhtml' ,
				lang = 'en')
        chapter.set_content(str(article_soup.font))
        book.add_item(chapter)
        book.toc.append(chapter)
        book.spine.append(chapter)


#book.spine.append(nav_css)

#create the eboook
epub.write_epub('pgtest.epub' , book)
print(' done ')
if __name__ == "__name__":
    scrape_articles("http://paulgraham.com/articles.html")

