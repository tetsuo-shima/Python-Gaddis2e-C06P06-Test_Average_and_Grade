__author__ = 'dwight'

# Write a program that asks the user to enter five test scores. The program should display a letter grade for each
# score and the average test score. Write the following functions in the program:
# • calc_average — This function should accept five test scores as arguments and return the average of the scores.
# • determine_grade — This function should accept a test score as an argument and return a letter grade for the score,


def main():
    test_scores = collect_scores()
    print()
    show_grades(test_scores)
    print()
    print('Test Average:', calc_average(test_scores))


def collect_scores():
    number_of_tests = 5

    scores = [0] * number_of_tests

    for index in range(len(scores)):
        test_score = int(input('Enter score for test #' + str(index + 1) + ': '))
        scores[index] = verify_test_score(test_score)
    return scores


def calc_average(grade_list):
    grade_total = 0

    for grade in grade_list:
        grade_total += grade

    return grade_total / len(grade_list)


def show_grades(grade_list):
    print('TEST GRADES')
    print('-----------')
    for index in range(len(grade_list)):
        print('Test #', index + 1, ': ', determine_grade(grade_list[index]), sep='')


def determine_grade(score):
    if score < 60:
        return 'F'
    elif score < 70:
        return 'D'
    elif score < 80:
        return 'C'
    elif score < 90:
        return 'B'
    else:
        return 'A'


def verify_test_score(score):
    while score < 0 or score > 100:
        print('Invalid test score. Please enter score between 0 and 100.')
        score = int(input('Enter new score: '))

    return score


main()