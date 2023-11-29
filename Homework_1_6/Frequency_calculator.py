note_1 = float(input('Please input a frequency in Hz: '))

i = 0

note = [0] * 5

r = 2 ** (1 / 12)

while i < 5:
    t = i + 1
    note[i] = note_1 * r ** i
    i += 1

print('{:.2f} {:.2f} {:.2f} {:.2f} {:.2f}'.format(note[0], note[1], note[2], note[3], note[4]))
