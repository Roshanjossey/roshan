class Export(object):
    '''Export details to different formats'''

    def __init__(self, film):
        self.film_details = film.provide_values()

    def export(self):  # Abstract method, defined by convention only
        raise NotImplementedError('Subclasses will implement this method')
