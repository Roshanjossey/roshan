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


class ExportToText(object):
	"""Exports details of film to text file"""
	def __init__(self, film):
		_file = open('film_details.txt', 'w')
		_file.write(
			'''Name: {0} \n
			   Run time: {1} \n
			   Language: {2} \n
			   Lead Actor: {3} \n
			   Genre: {4} \n'''.format(
			   	                       film.name,
			   	                       film.run_time,
			   	                       film.language,
			   	                       film.lead_actor,
			   	                       film.genre))
		
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
	print 'Which format should the data be converted to?'
	print '    1. Text\n    2. Pdf\n    3. Don\'t sweat it\n Enter your option'
	option = input()
	if option == 1:
		ExportToText(movie)

if __name__ == '__main__':
	main()