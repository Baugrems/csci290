def countCourses(inputList):
    courses = {}
    studCourses = {}   #empty maps for setup. One for courses and one for students
    for course in inputList: 
        course = course.split() # split the input and separate student from course
        student = course[0] + " " + course[1]
        course = course[-1]
        if student not in studCourses: # if student is not in map, add them
            studCourses[student] = []
        if course in studCourses[student]: # if they already added this course, skip and continue loop
            continue
        else:
            studCourses[student].append(course) # put the course in the students list of courses
        if course not in courses: # now we add course to our courses map if it isnt there yet
            courses[course] = 1
        else:
            courses[course] += 1 # or we increment the count in the map for that course
        courseKeys = list(courses.keys())
        courseKeys.sort() # sort all the courses for correct ordering
    for key in courseKeys: # print them all with their accumulated values
        print(key, courses[key])


amt = int(input())
courseList = []
for n in range(amt):
    courseList.append(input())
countCourses(courseList)
    

