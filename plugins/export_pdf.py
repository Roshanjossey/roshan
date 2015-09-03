import export
from reportlab.pdfgen import canvas


class ExportToPdf(object):
    '''Exports details of film to pdf file

    Returns an instance of ExportToPdf to export data to pdf format'''
    def __init__(self, film):
        self.name = film['name']
        self.run_time = film['run_time']
        self.language = film['language']
        self.lead_actor = film['lead_actor']
        self.genre = film['genre']

    def export(self):
        '''Exports details of film to pdf file

        Data will be exported to pdf format and stored in
        a file named film_details.pdf in the same directory'''
        _canvas = canvas.Canvas('film_details.pdf')
        _canvas.drawString(1, 825, 'Name: {}'.format(self.name))
        _canvas.drawString(1, 800, 'Run time: {} minutes'.format(self.run_time))
        _canvas.drawString(1, 775, 'Language: {}'.format(self.language))
        _canvas.drawString(1, 750, 'Lead actor: {}'.format(self.lead_actor))
        _canvas.drawString(1, 725, 'Genre: {}'.format(self.genre))
        _canvas.save()