intake = int(input('How much caffeine have you had: '))

level_1 = intake / 2
level_2 = level_1 / 2
level_3 = level_2 / 4

print('After 6 hours:', format(level_1, '.2f'), 'mg\nAfter 12 hours:', format(level_2, '.2f'), 'mg\nAfter 24 hours:',
      format(level_3, '.2f'), 'mg')
