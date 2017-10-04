#!/usr/bin/python

import sys

def power(a, powerTo):
	count = 0
	final = a
	while (count < powerTo):
		print 'Number ', count, ' has value ', final
		final = final * a
		count = count + 1

	return final

print power(input("Enter number: "), input("Enter power number: "))




