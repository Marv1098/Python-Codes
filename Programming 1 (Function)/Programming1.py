def calculate_average (score1, score2, score3):
    average = ( score1 + score2 + score3) / 3
    return average

def assign_grade(score):
    if score < 60:
        return 'F'
    elif score < 70:
        return 'D'
    elif score < 80:
        return 'C'
    elif score < 90:
        return 'B'
    elif score < 101:
        return 'A'

def get_scores ():
    score1 = float(input('Enter your score 1: '))
    while score1 < 0:
        print('Error: input must be positive.')
        score1 = float(input('Enter your score 1: '))

    score2 = float(input('Enter your score 2: '))
    while score2 < 0:
        print('Error: Input must be positive.')
        score2 = float(input('Enter your score 2: '))

    score3 = float(input('Enter your score 3: '))
    while score3 < 0:
        print('Error: Input must be positive.')
        score3 = float(input('Enter your score 3: '))

    return score1, score2, score3

def show_results(average, grade):
    print('Average:', average)
    print('Grade: ', grade)

def main():
    score1, score2, score3 = get_scores()
    average = calculate_average(score1, score2, score3)
    grade = assign_grade(average)
    show_results(average, grade)

main()
