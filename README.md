## Bibo
Bibo is a simple python script that turn all [Paul Graham 
essays](http://paulgraham.com/articles.html) to an e-book 
with([.epub](https://en.wikipedia.org/wiki/EPUB)) extension that works with Kindle or any 
e-books reader app/device.
### Installing
clone this repo.
``` 
git clone https://github.com/abdullahMosibah/bibo.git cd bibo
``` 

and create a new enviroment and activate it.
``` 
virtualenv -p python3 venv source 
venv/bin/activate
```

then install all prerequisite libraries
``` 
pip install -r 
requirements.txt 
``` 

and then run main_bibo.py 
```
python main_bibo.py
```

## Built With
* [requests](https://github.com/psf/requests) - A simple, yet elegant HTTP library.
* [ebooklib](https://github.com/aerkalov/ebooklib) - Python E-book library for handling books 
in EPUB2/EPUB3 format

## Authors
* **Abdullah Mosibah** - *Initial work* - [Github](https://github.com/abdullahMosibah)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for 
details

## Acknowledgments
