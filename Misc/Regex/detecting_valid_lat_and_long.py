#!/usr/bin/py

import re

def valid_lat_long(s):
  match = re.findall(r'\('
                        r'([+-]?[0-9]{1,2}(?:\.[0-9]+)?)'  
                        r', '
                        r'([+-]?[0-9]{1,3}(?:\.[0-9]+)?)'
                        r'\)',
                        s)
  print match
  if match:
    lat, lon = match[0]
    if -90 <= float(lat) <= 90 and -180 <= float(lon) <= 180:
      return 'Valid'
    else:
      return 'Invalid'

    
if __name__ == '__main__':
  n = input()
  for _ in range(n):
    print valid_lat_long(raw_input().strip())


