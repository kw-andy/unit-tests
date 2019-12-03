default = object()
def toto(a=default):
    if a is default:
        a = []
    a.append('toto')
    return a