scores=int(input('Please enter your score: '))
def determine_grade(scores):
    if scores >= 80 and scores<= 100:
        return 'A'
    elif scores >= 75 and scores<= 79:
        return 'B+'
    elif scores >= 70 and scores<= 74:
        return 'B'
    elif scores >= 65 and scores<= 69:
        return 'C+'
    elif scores >= 60 and scores<= 64:
        return 'C'
    elif scores >= 55 and scores<= 59:
        return 'D+'
    elif scores >= 50 and scores<= 54:
        return 'D'
    else:
        return 'F'
print('You got',determine_grade(scores))