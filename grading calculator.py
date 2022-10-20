print("\n\n\n")
print('\n\t\t\t\t\tThe Republic of The Union Of Myanmar\t\t\t\t\t\t\t\t\n')
print('\n\t\t\t\t\tTechnological University Of Yangon\t\t\t\t\t\t\t\t\n')
print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tDepartment of Information Technology\t\t\t\t\t\t\t\n')
print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tGrading System Calculator\t\t\t\t\t\t\t\n')


def grading(marks):
    for i in range(0, len(marks), 1):
        mark = marks[i]
        mark = int(mark)
        if 95 <= mark <= 100:
            grades.append('A+')
        elif 80 <= mark <= 94:
            grades.append('A')
        elif 60 <= mark <= 79:
            grades.append('B')
        elif 40<= mark <=59:
            grades.append('C')
        elif 20<= mark <=39:
            grades.append("Failed")
        else:
            grades.append('Try again better')


def getmark(sub):
    for i in range(0, 6):
        marks.append(input(sub[i]+ ' marks: '))
    return marks


while True:
    grades = []
    marks=[]
    year = input('To calculate your grade start typing your year :  ')
    if year == 'first':
        name=input('Your Name: ')
        roll=input('Roll Number: ')
        sub = ['Myanmar', 'English', 'Mathematics','Physics', 'Chemstry', 'IT Subject']
        grading(getmark(sub))
        print("**************************************************************************************")
        print(year +" year")
        print('Your name is  ' + name)
        print('Roll Number is '+roll)
        print('Your grades are as below :')
        for i in range(0,6,1):
            print(sub[i] +"=" +"\t" +grades[i])
    

    elif year=='second':
        name=input('Student Name: ')
        roll=input('Roll Number: ')
        sub = ['English', 'Mathematics','IT subject-1', 'IT subject -2', 'IT subject-3','Major-1 ']
        grading(getmark(sub))
        print("**************************************************************************************")
        print(year +" year")
        print('Student Name is ' + name)
        print('Roll Number is '+roll)
        print('Your grades are as below :')
        for i in range(0,6,1):
            print(sub[i] +' ' +"\t" +grades[i])

    elif year=='third':
        name=input('Student Name: ')
        roll=input('Roll Number:')
        sub = ['English','IT subject-1','IT subject-2','IT subject-3','Major 1','Major-2']
        grading(getmark(sub))
        print("**************************************************************************************")
        print(year +" year")
        print('Student Name is ' + name)
        print('Roll Number is '+roll)
        print('Your grades are as below :')
        for i in range(0,6,1):
            print(sub[i] +' ' +"\t" +grades[i])

    elif year=='fourth':
        name=input('Student Name: ')
        roll=input('Roll Number: ')
        sub = ['IT subject-1','IT subject-2','IT subject-3','Major 1','Major-2','Major-3']
        grading(getmark(sub))
        print("**************************************************************************************")
        print(year +" year")
        print('Student Name is ' + name)
        print('Roll Number is '+roll)
        print('Your grades are as below :')
        for i in range(0,6,1):
            print(sub[i] +' ' +"\t" +grades[i])

    else:
        print("Enter year only: ")
        continue
    print("*************************************************************************************")
    opt = input('Do you want to calculate more(y/n)?')
    if opt == 'y':
        continue
    else:
        break


