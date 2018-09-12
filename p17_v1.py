"""
# Number letter counts
# https://projecteuler.net/problem=XXX
# 9-8-2018, 22:07 - 9-9-2018, 00:22

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example,
342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""

# Timing Tools
import time
start = time.time()

"""Start Here"""

ones = {
    '0':' ',
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine',
}
teens = {
    '10':'ten',
    '11':'eleven',
    '12':'twelve',
    '13':'thirteen',
    '14':'fourteen',
    '15':'fifteen',
    '16':'sixteen',
    '17':'seventeen',
    '18':'eighteen',
    '19':'nineteen'
}
second_dig = {
    '2':'twenty',
    '3':'thirty',
    '4':'forty',
    '5':'fifty',
    '6':'sixty',
    '7':'seventy',
    '8':'eighty',
    '9':'ninety'
}

def num_word(x):
    number = ''
    if len(x) == 4:
        number = number + (ones[x[0]])
        number = number + '-thousand '
        x.pop(0)
    if len(x) == 3:
        if x[0] == '0':
            x.pop(0)
        else:
            number = number + (ones[x[0]])
            number = number + ('-hundred ')
            if not (x[1] == '0' and x[2] == '0'):
                number = number + 'and '
            x.pop(0)
    if len(x) == 2:
        if x[0] == '0':
            x.pop(0)
        elif x[0] == '1':
            teen = str(x[0]+x[1])
            number = number + (teens[teen])
            x.pop(0)
            x.pop(0)
        else:
            number = number + (second_dig[x[0]] + '-')
            x.pop(0)
    if len(x) == 1:
        number = number + (ones[x[0]])
        x.pop(0)
    return number

# Testing (by passing a single number)
# sum = 0
# word =list(input())
# word = num_word(word)
# word = word.replace(' ', '')
# word = word.replace('-', '')
# print(f'word:{word}, {len(word)}')

sum = 0
for num in range(1,1001):
    word = num_word(list(str(num)))
    # print(word)
    word = word.replace(' ', '')
    word = word.replace('-', '')
    sum += len(word)

print(f'Answer: {sum}')
print(f'Clocked in at {time.time()-start} second(s)')
