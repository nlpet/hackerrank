from collections import defaultdict

def is_palindrome(string):
	occ = defaultdict(int)
	for char in string:
		occ[char] += 1
		
	odd = 0
	for v in occ.values():
		if v % 2 != 0: odd += 1
		
	if odd <= 1: return True
	else: return False
		
string = raw_input().lower()
found = is_palindrome(string)


if not found:
    print("NO")
else:
    print("YES")
