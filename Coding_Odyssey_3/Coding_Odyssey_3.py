file = open('moby_dick.rtf', 'r')

print(file.read())

print(file.closed)

file.close()

print(file.closed)
