#!/bin/python

import sys

def braces(values):
    matching_pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    
    braces_stack = []
    for ch in values:
        matching_brace = matching_pairs.get(ch)
        if matching_brace:
            braces_stack.append(ch)
        elif not braces_stack or matching_pairs.get(braces_stack.pop()) != ch:
            return False
    return True if not braces_stack else False


t = int(raw_input().strip())
for a0 in xrange(t):
    s = raw_input().strip()
    if braces(s):
        print 'YES'
    else:
        print 'NO'
