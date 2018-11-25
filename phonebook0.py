# using only the dictionary data structure to build a phone book

def phone_book(names, cities):
    '''
        Function takes two lists (names and cities) and returns a simple phonebook dictionary object.
    '''
    result = dict()
    if len(names) == len(cities):
        for i in range(len(names)):
            result[names[i]] = cities[i]
        return result
    else:
        return 'Lengths of names and their current cities don\'t match.'
    


if __name__ == "__main__":
    names = ['Hannes', 'Karl', 'Mareile', 'Kevin', 'Andrew', 'Lauren', 'Conrad', 'Megan', 'Nick', 'Rodrigo']
    cities = ['Stockholm', 'Uppsala', 'Heidelberg', 'Munich', 'New Castle', 'Southport', 'Southport', 'Osaka', 'Amsterdam', 'Washington']

    print(phone_book(names, cities))
