import copy


def remove_every_nth(lst, n):
    del lst[n - 1::n]
    return lst


def normalize(data: [], field: str):
    full_field_set = list(set(range(data[-1][field] + 1)))
    normalized_cursor = list(map(lambda value: {field: value}, full_field_set))
    normalized_list = []

    last_useful_data = copy.deepcopy(data[0])
    for cursor in normalized_cursor:
        existing_data = next((x for x in data if x[field] == cursor[field]), None)
        if existing_data is not None:
            last_useful_data = copy.deepcopy(existing_data)
            normalized_list.append(existing_data)
        else:
            last_useful_data[field] = cursor[field]
            normalized_list.append(copy.deepcopy(last_useful_data))

    return remove_every_nth(normalized_list, 2)


