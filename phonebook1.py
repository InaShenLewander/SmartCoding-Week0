# Attemping to use both dictionary and object to make a phone book.

class Contact:
    def __init__(self, name, email, current_city):
        self.name = name
        self.email = email
        self.current_city = current_city
    
    def __str__(self):
        return '{0}/{1}/{2}'.format(self.name, self.email, self.current_city)

def phone_book(contacts):
    '''
        takes a list of contact objects and returns a dictionary of contacts.
    '''
    result = dict()
    for contact in contacts:
        result[contact.name] = [contact.email, contact.current_city]
    return result

def make_contacts(names, emails, cities):
    '''
        takes a list of raw data (names, emails and cities) and returs a list of contact objects.
    '''
    contacts = []
    for i in range(len(names)):
        contacts.append(Contact(names[i], emails[i] , cities[i]))
    return contacts


if __name__ == "__main__":
    names = ['Hannes', 'Karl', 'Mareile', 'Kevin', 'Andrew', 'Lauren', 'Conrad', 'Megan', 'Nick', 'Rodrigo']
    cities = ['Stockholm', 'Uppsala', 'Heidelberg', 'Munich', 'New Castle', 'Southport', 'Southport', 'Osaka', 'Amsterdam', 'Washington']
    emails = ['abc@Gmail.com', 'abc@Gmail.com', 'abc@Gmail.com', 'abc@Gmail.com', 'abc@Gmail.com', 'abc@Gmail.com', 'abc@Gmail.com', 'abc@Gmail.com', 'abc@Gmail.com', 'abc@Gmail.com']
    
    contacts = make_contacts(names, emails, cities)
    my_phonebook = phone_book(contacts)

    # Below are some operations with the phone book.

    # Print out the entire phone book.
    print(my_phonebook)
    
    # See the contacts' names.
    for key in my_phonebook.keys():
        print(key)

    # Look up a specific entry
    print(my_phonebook.get('Kevin'))

    # Print out all the entries in alphabetically sorted order
    for k, v in sorted(my_phonebook.items()):
        print('{0}: {1}, {2}'.format(k, v[0], v[1]))
