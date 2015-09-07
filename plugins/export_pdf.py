from plugins.export import Export
from reportlab.pdfgen import canvas


class ExportToPdf(Export):
    '''Exports details of film to pdf file

    Returns an instance of ExportToPdf to export data to pdf format'''

    def export(self):
        '''Exports details of film to pdf file

        Data will be exported to pdf format and stored in
        a file named film_details.pdf in the same directory'''
        
        _canvas = canvas.Canvas('film_details.pdf')
        y_co_ordinate = 825
        for field in self.film_details:
            _canvas.drawString(1, y_co_ordinate, '{}: {}'.format(field, self.film_details[field]))
            y_co_ordinate -= 25
        _canvas.save()