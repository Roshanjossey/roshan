import film
import inspect
import glob, imp
from os.path import join, basename, splitext

def importPluginModulesIn(directory):
    modules = {}
    for path in glob.glob(join(directory,'[!_]*.py')): # list .py files not starting with '_'
        name, ext = splitext(basename(path))
        modules[name] = imp.load_source(name, path)
    return modules


def main():
    print 'Enter name of film'
    name = raw_input()
    print 'Enter run time in minutes:'
    run_time = input()
    print 'Enter language:'
    language = raw_input()
    print 'Enter lead_actor:'
    lead_actor = raw_input()
    print 'Enter genre:'
    genre = raw_input()
    movie = {}
    movie['name'] = name
    movie['run_time'] = run_time
    movie['language'] = language
    movie['lead_actor'] = lead_actor
    movie['genre'] = genre
    # movie = Film(name, run_time, language, lead_actor, genre)
    print 'Which format should the data be converted to?'
    plugins = importPluginModulesIn('plugins')
    for x in plugins:
        print x
    print 'For example input \'export_pdf\''
    format = raw_input()
    for name, obj in inspect.getmembers(plugins[format]):
        if inspect.isclass(obj):
            FormatClass = getattr(plugins[format], name)  # I'm using introspection here
            # Looks for an attribute of plugins module with name input by user (format)
            movie_export = FormatClass(movie)  # Creates an instance of desired class
            movie_export.export()  # Calls function for exporting to required format

if __name__ == '__main__':
    main()
