## Movie Aggregator

demo of typical excecution
```
(roshan)nishika@nishika:~/project1$ python film.py 
Enter name of film:
Satantango
Enter run time in minutes:
435
Enter language:
Hungary
Enter lead_actor:
Bela Tarr
Enter genre:
Drama
Which format should the data be converted to?
ExportToPdf
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
$ python film.py
```
give the neccessary details and choose an option corresponding file will be created in same directory.
Options are name of export classes in plugins.py file like ExportToPdf, ExportToText

It can be made extensible by adding classes to plugins.py file

example
```
class ExportToHtml(Export):
    '''Exports details of film to html file'''
    def __init__(self, film):
        self.name = film.name
        self.run_time = film.run_time
        self.language = film.language
        self.lead_actor = film.lead_actor
        self.genre = film.genre

    def export(self):
        _file = open('film_details.html', 'w')
        _file.write(('Name: {0} </br>'
                     'Run time: {1} </br>'
                     'Language: {2} </br>'
                     'Lead Actor: {3} </br>'
                     'Genre: {4} </br>').format(self.name,
                                             self.run_time,
                                             self.language,
                                             self.lead_actor,
                                             self.genre))
```