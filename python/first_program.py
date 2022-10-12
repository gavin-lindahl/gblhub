# this is going to be my first python program

def average():
    score1 = int(input("Input score number one: "))
    score2 = int(input("Input score number two: "))
    score3 = int(input("Input score number three: "))
    student_average = int((score1+score2+score3)/3)
    return student_average

if __name__ == '__main__':
    average_score = average()

print(f'Average Grade: {average_score}')