# Compute final course grades for students based on percentage scores using a function.


score = float(input("Enter the numerical score: "))


def letterGrade(score):

    if score >= 95:
        return 'A+'

    elif score >= 90 and score < 95:
        return 'A'

    elif score >= 85 and score < 90:
        return 'A-'

    elif score >= 80 and score < 85:
        return 'B+'

    elif score >= 75 and score < 80:
        return 'B'

    elif score >= 70 and score < 75:
        return 'B-'

    elif score >= 65 and score < 70:
        return 'C+'

    elif score >= 60 and score < 65:
        return 'C'

    elif score >= 55 and score < 60:
        return 'C-'

    else:
        return 'F'


result = letterGrade(score)

print("The letter grade for %.2f percent is %s" % (score, result))
