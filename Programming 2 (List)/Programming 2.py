def get_scores():
    scores_list = []
    num_scores = int(input('How many test scores: '))
    for index in range (num_scores):
        print('Test score #', index+1)
        test = float(input())
        while test < 0:
            print('Input Error: Enter a positive number')
            print('Test score #', index + 1)
            test = float(input())
        scores_list.append(test)
    return scores_list

def calculate_average(scores_list):
    total = 0
    for item in scores_list:
        total += item
    lowest = min(scores_list)
    average = (total - lowest)/(len(scores_list)-1)
    return total, average

def determine_grade(score):
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

def show_result(average, grade):
    print('Average:', average)
    print('Grade:', grade)

def main():
    scores = get_scores()
    print(scores)
    total, average = calculate_average(scores)
    grade = determine_grade(average)
    show_result(average, grade)

main()
