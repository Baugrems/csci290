def countCourses(inputList):
    courses = {}
    studCourses = {}   
    for course in inputList:
        course = course.split()
        student = course[0] + " " + course[1]
        course = course[-1]
        if student not in studCourses:
            studCourses[student] = []
        if course in studCourses[student]:
            continue
        else:
            studCourses[student].append(course)
        if course not in courses:
            courses[course] = 1
        else:
            courses[course] += 1
        courseKeys = list(courses.keys())
        courseKeys.sort()
    for key in courseKeys:
        print(key, courses[key])


amt = int(input())
courseList = []
for n in range(amt):
    courseList.append(input())
countCourses(courseList)
    

