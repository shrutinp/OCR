# Python program to demonstrate
# glob using different wildcards

import glob

print('Named explicitly:')
for name in glob.glob('/Users/Admin/Desktop/TextRecog/1.jpg'):
	print(name)

# Using '*' pattern
print('\nNamed with wildcard *:')
for name in glob.glob('/Users/Admin/Desktop/TextRecog/*'):
	print(name)

# Using '?' pattern
print('\nNamed with wildcard ?:')
for name in glob.glob('/Users/Admin/Desktop/TextRecog/*.txt'):
	print(name)

# Using [0-9] pattern
print('\nNamed with wildcard ranges:')
for name in glob.glob('/Users/Admin/Desktop/TextRecog/*[0-9].*'):
	print(name)
