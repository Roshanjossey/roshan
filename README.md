## Movie Aggregator

demo of typical excecution

(roshan)nishika@nishika:~/project$ python film.py 
Enter name of film:
Play Time
Enter run time in minutes:
101
Enter language:
French
Enter lead_actor:
Tati
Enter genre:
Comedy
Play Time 101 French Tati Comedy
Which format should the data be converted to?
    1. Text
    2. Pdf
    3. Don't sweat it
 Enter your option
2
(roshan)nishika@nishika:~/project$ ls
film_details.pdf  film.py  README.md

I've used virtual environment to make this project easily portable
To run this you should have virtualenv and virtualenvwrapper installed
following are links regarding thier installation
[virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)

To activate virtual environment wrapper use

$ export WORKON_HOME=This_directory/.virtualenvs

where This_directory is path to the repository

$ source /usr/local/bin/virtualenvwrapper.sh
$ workon roshan

To run use
$ python film.py

give the neccessary details and choose an option corresponding file will be created in same directory