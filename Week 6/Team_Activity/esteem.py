'''
Brennon Laney
05/27/21
Team Activity 
'''

print('This program is an implementation of the Rosenberg Self-Esteem Scale')
print('This program will show you ten statements that you could possibly')
print('apply to yourself. Please rate how much you agree with each of the')
print('statements by responding with one of these four letters:')
print()

print('D means you strongly disagree with the statement.')
print('d means you disagree with the statement.')
print('a means you agree with the statement.')
print('A means you strongly agree with the statement.')


def main():
    scores01 = []
    scores02 = []

    scores01.append(input('1. I feel that I am a person of worth, at least on'\
         'an equal plane with others. Enter D, d, a, or A: '))
    scores01.append(input('2. I feel that I have a number of good qualities.' \
         'Enter D, d, a, or A: '))
    scores02.append(input('3. All in all, I am inclined to feel that I am a failure.' \
         'Enter D, d, a, or A: '))
    scores01.append(input('4. I am able to do things as well as most other people.' \
         'Enter D, d, a, or A: '))
    scores02.append(input('5. I feel I do not have much to be proud of.' \
         'Enter D, d, a, or A: '))
    scores01.append(input('6. I take a positive attitude toward myself.' \
         'Enter D, d, a, or A: '))
    scores01.append(input('7. On the whole, I am satisfied with myself.' \
         'Enter D, d, a, or A: '))
    scores02.append(input('8. I wish I could have more respect for myself.' \
         'Enter D, d, a, or A: '))
    scores02.append(input('9. I certainly feel useless at times.' \
         'Enter D, d, a, or A: '))
    scores02.append(input('10. At times I think I am no good at all.' \
         'Enter D, d, a, or A: '))



    score = calculate_score(scores01, scores02)

    print(f'Your score is {score}')
    print('A score below 15 may indicate problematic low self_esteem')

def calculate_score(scores01, scores02):
    '''
    This here is going to take the items in scores01 and scores02
    and based on whether it is an 'A', 'a', 'd', and 'D' it will add a value
    
    in scores01:
        A = 3
        a = 2
        d = 1
        D = 0

    in scores02:
        A = 0
        a = 1
        d = 2
        D = 3
    '''
    total_score = 0
    for i in scores01:
        
        if i == 'A':
            total_score += 3

        elif i == 'a':
            total_score += 2

        elif i == 'd':
            total_score += 1

        elif i == 'D':
            total_score += 0

    for i in scores02:
        
        if i == 'D':
            total_score += 3

        elif i == 'd':
            total_score += 2

        elif i == 'a':
            total_score += 1

        elif i == 'A':
            total_score += 0

    return total_score
main()