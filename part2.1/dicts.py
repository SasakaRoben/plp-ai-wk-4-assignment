
# Automated implementation of sorting dictionaries by a specified key
def sort_dicts_by_key(data, key):
    return sorted(data, key=lambda x: x[key])


# Manual implementation of sorting dictionaries by a specified key
def sort_dicts_by_key_manual(data, key):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i][key] > data[j][key]:
                data[i], data[j] = data[j], data[i]
    return data
