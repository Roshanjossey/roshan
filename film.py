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
	print movie.name, movie.run_time, movie.language, movie.lead_actor, movie.genre

if __name__ == '__main__':
	main()