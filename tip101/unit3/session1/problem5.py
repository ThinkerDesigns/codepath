def first_unique_char(my_str):
    freq = {}
    for i,character in enumerate(my_str):
        if character not in freq:
            freq[character] = 1
        else:
            freq[character] += 1
    for i,character in enumerate(my_str):
        if freq[character] == 1:
            return i
    return -1
my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))