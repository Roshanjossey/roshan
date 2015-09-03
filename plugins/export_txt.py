import export


class ExportToText(object):
    '''Exports details of film to text file

    Returns an instance of ExportToText to export data to txt format'''
    def __init__(self, film):
        self.name = film['name']
        self.run_time = film['run_time']
        self.language = film['language']
        self.lead_actor = film['lead_actor']
        self.genre = film['genre']

    def export(self):
        '''Exports details of film to text file

        Data will be exported to txt format and stored in
        a file named film_details.txt in the same folder'''
        _file = open('film_details.txt', 'w')
        _file.write(('Name: {0} \n'
                     'Run time: {1} \n'
                     'Language: {2} \n'
                     'Lead Actor: {3} \n'
                     'Genre: {4} \n').format(self.name,
                                             self.run_time,
                                             self.language,
                                             self.lead_actor,
                                             self.genre))