import plugins


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


def main():
    print 'Enter name of film:'
    name = raw_input()
    print 'Enter run time in minutes:'
    run_time = input()
    print 'Enter language:'
    language = raw_input()
    print 'Enter lead_actor:'
    lead_actor = raw_input()
    print 'Enter genre:'
    genre = raw_input()
    movie = Film(name, run_time, language, lead_actor, genre)
    print 'Which format should the data be converted to?'
    print 'For example input \'ExportToPdf\''
    format = raw_input()
    FormatClass = getattr(plugins, format)  # I'm using introspection here
    # Looks for an attribute of plugins module with name input by user (format)
    movie_export = FormatClass(movie)  # Creates an instance of desired class
    movie_export.export()  # Calls function for exporting to required format

if __name__ == '__main__':
    main()
