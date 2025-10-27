from .colvar import Colvar

all = ["read"]

def read(filename: str) -> Colvar:
    '''
    Read a PLUMED-style colvar file and return a Colvar object.

    :param filename: Path to the colvar file.
    :return: A Colvar object containing the data from the file.
    '''
    cv = Colvar()
    cv.read(filename)
    return cv