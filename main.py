from film import Film
import re
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
    film = Film(name, run_time, language, lead_actor, genre)
    print 'Which format should the data be converted to?'
    print 'Following plugins available'
    plugins = importPluginModulesIn('plugins')
    options = [x for x in plugins if re.match(r'export_\w+', x)]
    for option_no, option_name in enumerate(options):
        format_name = re.match(r'export_(\w+)', option_name)
        format_name = format_name.group(1)
        print option_no + 1, format_name
    print 'Enter and option number'
    _format = options[input() -1]
    print _format
    for name, obj in inspect.getmembers(plugins[_format])[1:]:
        if inspect.isclass(obj):
            FormatClass = getattr(plugins[_format], name)  # I'm using introspection here
            # Looks for required class in selected module in plugins package
            # _format is name of selected module, name is name of class
            movie_export = FormatClass(film)  # Creates an instance of desired class
            movie_export.export()  # Calls function for exporting to required format

if __name__ == '__main__':
    main()
