from sys import stdin

data = [x.strip() for x in stdin.readlines()]

set_of_countries = set()

for c in data[1:]:
    set_of_countries.add(c)


print(len(set_of_countries))
