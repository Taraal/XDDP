from xddp.pokemon.models import Pokemon

def importAll():
    """
    Gets all the Pokemon from the API and stores them locally
    :return: returns the getAll() method
    """
    for i in range(1,152):
        Pokemon.ImportOne(i)

