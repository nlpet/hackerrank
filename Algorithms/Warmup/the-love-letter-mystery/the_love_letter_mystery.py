import string
import sys
from math import fabs


#input = ['5\n','pue\n','heubsbn\n','feazhaxpux\n','hmhcy\n','tmp\n']
input = sys.stdin.readlines()
alph = string.ascii_lowercase

def count_mismatches(s1,s2):
	if len(s1) == 1: return int(fabs(alph.index(s2) - alph.index(s1)))
	else:
		total = 0
		s2 = s2[::-1]
		for i in range(len(s1)):
			total += int(fabs(alph.index(s2[i]) - alph.index(s1[i])))
		return total

for s in input[1:]:
	s = s.strip()
	if s == s[::-1]: print 0
	else:
		if len(s) % 2 == 0:
			print count_mismatches(s[:len(s)/2],s[len(s)/2:])
		else:
			print count_mismatches(s[:len(s)/2],s[len(s)/2+1:])
	

