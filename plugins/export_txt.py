from plugins.export import Export


class ExportToText(Export):
    '''Exports details of film to text file

    Returns an instance of ExportToText to export data to txt format'''

    def export(self):
        '''Exports details of film to text file

        Data will be exported to txt format and stored in
        a file named film_details.txt in the same folder'''
        _file = open('film_details.txt', 'w')
        for field in self.film_details:
            _file.write('{}: {}\n'.format(field, self.film_details[field]))