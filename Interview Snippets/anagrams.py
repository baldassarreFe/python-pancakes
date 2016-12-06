import itertools

a = ["ehi", "married", "lives", "admirer" , "hei", "elvis"]

print(sorted(a, key = lambda s : sorted(s)))

anagrams = {}
for key, group in itertools.groupby(a, key = lambda s : sorted(s)):
    anagrams["".join(key)] = anagrams.get("".join(key), []).append(list(group))

print(anagrams)


