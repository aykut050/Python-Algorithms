def get_all_substring_of_string(t):
    res = [t[i: j] for i in range(len(t))
          for j in range(i + 1, len(t) + 1)]
    
    return res

def find_max(t,z):
    all_substrings = get_all_substring_of_string(t)

    max_value = 0

    for all_substrings_item in all_substrings:
        count = z.count(all_substrings_item)
        total = len(all_substrings_item) * count

        if max_value < total:
            max_value = total

    return max_value

print(find_max("acldm1labcdhsnd","shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa"))