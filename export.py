class Export(object):
    '''Export details to different formats'''

    def __init__(self, film):
        self.name = film['name']
        self.run_time = film['run_time']
        self.language = film['language']
        self.lead_actor = film['lead_actor']
        self.genre = film['genre']

    def export(self):  # Abstract method, defined by convention only
        raise NotImplementedError('Subclasses will implement this method')
