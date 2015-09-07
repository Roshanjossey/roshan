from collections import OrderedDict


class Film(object):
    ''' Attributes:
            name: A string, name of the Film
            run_time: integer runtime of film in minutes
            language: string , language spoken in the film
            lead_actor: string, actor who plays protagonist
            genre: string, genre(category of film)
    '''
    def __init__(self, name, run_time, language, lead_actor, genre):
        ''' Return a film object with values of arguments assigned to
        object fields'''
        self.name = name
        self.run_time = run_time
        self.language = language
        self.lead_actor = lead_actor
        self.genre = genre

    def provide_values(self):
        film_details = OrderedDict()
        film_details['Name'] = self.name
        film_details['Run time'] = self.run_time
        film_details['language'] = self.language
        film_details['lead_actor'] = self.lead_actor
        film_details['genre'] = self.genre
        return(film_details)