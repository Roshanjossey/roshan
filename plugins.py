from reportlab.pdfgen import canvas


class Export(object):
    '''Export details to different formats'''

    def __init__(self, film):
        self.name = film.name
        self.run_time = film.run_time
        self.language = film.language
        self.lead_actor = film.lead_actor
        self.genre = film.genre

    def export(self):  # Abstract method, defined by convention only
        raise NotImplementedError('Subclasses will implement this method')


class ExportToText(Export):
    '''Exports details of film to text file'''
    def __init__(self, film):
        self.name = film.name
        self.run_time = film.run_time
        self.language = film.language
        self.lead_actor = film.lead_actor
        self.genre = film.genre

    def export(self):
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


class ExportToPdf(Export):
    '''Exports details of film to pdf file'''
    def __init__(self, film):
        self.name = film.name
        self.run_time = film.run_time
        self.language = film.language
        self.lead_actor = film.lead_actor
        self.genre = film.genre

    def export(self):
        _canvas = canvas.Canvas('film_details.pdf')
        _canvas.drawString(1, 825, 'Name: {}'.format(self.name))
        _canvas.drawString(1, 800, 'Run time: {} minutes'.format(self.run_time))
        _canvas.drawString(1, 775, 'Language: {}'.format(self.language))
        _canvas.drawString(1, 750, 'Lead actor: {}'.format(self.lead_actor))
        _canvas.drawString(1, 725, 'Genre: {}'.format(self.genre))
        _canvas.save()