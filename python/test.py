# def duplicate_count(text):
#     set_one = set(text.lower())
#     set_two = set()
#     for i in set_one:
#         if i in set_one:
#             set_two.add(i)
#     return set_two

# print(set("abcde".lower()))
# print(duplicate_count("abcde"))
import collections
def duplicate_count(text):
    c = collections.Counter(text.lower())
    return len({x: count for x, count in c.items() if count > 1})
print(duplicate_count("Indivisibilities"))