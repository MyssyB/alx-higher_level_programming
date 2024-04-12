#!/usr/bin/python3

trial_one = ['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
trial_one[1] = 'one'
for i in trial_one:
    print(len(i))
print(trial_one[1])
