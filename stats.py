def sort_on(dict):
    return dict["num"]

def count_words(document):
    words = document.split()
    return len(words)

def count_characters(document):
    character_counts = {}

    for char in document:
        char = char.lower()
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    
    return character_counts

def sort_counts(count_dict):
    list_of_dicts = []

    for key in count_dict:
        new_dict = {
            "char": key,
            "num": count_dict[key]
        }
        list_of_dicts.append(new_dict)

    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts