import ebooklib 
from ebooklib import epub

book = epub.EpubBook()

book.set_identifier('PGtest')
book.set_title('PGtest')
book.set_language('en')

book.add_author('abdullahMosibah')
for i in range(6):
    c1 = epub.EpubHtml(title=f'introduction{i}' , file_name=f'chap_{i}.xhtml', lang = 'en')
    c1.set_content(u'<h1>introduction</h1><p>wdasdsadasdasdasdsadsaasdasdasdasdasd</p>')
    book.add_item(c1)
    book.toc.append(c1)
    book.spine.append(c1)

'''
c2 = epub.EpubHtml(title='second' , file_name='chap_02.xhtml', lang = 'en')
c2.set_content(u'<h1>dscohnd shit</h1><p>wdasdsadasdasdasdsadsaas</p>')
book.add_item(c2)
book.toc.append(c2)
book.spine.append(c2)
book.toc = (epub.Link('chap_02.xhtml', 'secondshit','secondsecondshit')
         , (
             epub.Section('Simplebook'), 
         (c2,)
         )
        )

'''
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

style= 'BODY {color:white;}'
nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css"
                        , media_type="text/css",content=style)

book.add_item(nav_css)
book.spine.append('nav')

epub.write_epub('PGtest.epub', book , {} ) 
              
