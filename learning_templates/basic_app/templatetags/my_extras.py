from django import templates



register = template.library()

def cut(value,arg):
    return value.replace(arg,'')

    register.filter('cut',cut)
