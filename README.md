## Movie Aggregator

demo of typical excecution
```
(roshan)nishika@nishika:~/project1$ python main.py
Enter name of film
Cache
Enter run time in minutes:
101
Enter language:
French
Enter lead_actor:
Haneke
Enter genre:
Drama
Which format should the data be converted to?
Following plugins available
1 txt
2 pdf
Enter and option number                                                              │
2
(roshan)nishika@nishika:~/project$ ls
film_details.pdf  film.py  README.md
```
I've used virtual environment to make this project easily portable
To run this you should have virtualenv and virtualenvwrapper installed
following are links regarding thier installation

[virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)

To activate virtual environment wrapper use

$ export WORKON_HOME=This_directory/.virtualenvs

where This_directory is path to the repository
```
$ source /usr/local/bin/virtualenvwrapper.sh
$ workon roshan

To run use
$ python main.py
```
give the neccessary details and choose an option corresponding file will be created in same directory.
Options are name of export classes in plugins.py file like ExportToPdf, ExportToText

It can be made extensible by adding modules to plugins folder

example add export_html.py to plugins folder with following code
```
class ExportToHtml(Export):
    '''Exports details of film to html file'''

    def export(self):
        _file = open('film_details.html', 'w')
        for field in self.film_details:
            _file.write('{}: {} <br>'.format(field, self.film_details[field]))
```
