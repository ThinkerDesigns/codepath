def print_pair(dictionary, target):
    for x in range(len(dictionary)):
        if target in dictionary:
            print( "Key: " + target + "\nValue: " + dictionary[target])
            break
        else:
            print( "That pair does not exist!")
            break
dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")