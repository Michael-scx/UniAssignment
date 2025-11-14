def calculate_average_enrollment(enrollment_list):
    if len(enrollment_list) == 0:
        return 0
    total = 0
    for num in enrollment_list:
        total+=num

    avg = total/len(enrollment_list)
    return avg
def find_most_popular_course(course_data):
    highest_avg = -1
    best_course = ""

    for item in course_data:
        course_code = item[0]
        dept = item[1]
        en_list = item[2]

        avg = calculate_average_enrollment(en_list)

        if avg>highest_avg:
            highest_avg=avg
            best_course = course_code
        elif avg == highest_avg:
            if course_code < best_course:
                best_course = course_code

    return best_course

def get_courses_in_department(course_data, dept_name):
    result = []
    for item in course_data:
        cc = item[0]          
        dept = item[1]

        if dept == dept_name:
            result.append(cc)
    n = len(result)
    for i in range(n):
        for j in range(0, n-i-1):
            if result[j]>result[j+1]:
                temp = result[j]
                result[j] = result[j+1]
                result[j+1] = temp

    return result

def get_department_enrollment_summary(course_data):
    departments = []
    totals = []

    for item in course_data:
        course_code = item[0]
        department = item[1]
        enrollments = item[2]

        
        index = -1
        for i in range(len(departments)):
            if departments[i] == department:
                index = i
                break

        if index == -1:   
            departments.append(department)

            total_students = 0
            for x in enrollments:
                total_students += x
            totals.append(total_students)

        else:  
            for x in enrollments:
                totals[index] +=x

    
    n = len(departments)
    for i in range(n):
        for j in range(0, n-i-1):
            if departments[j] > departments[j + 1]:
                
                temp = departments[j]
                departments[j] = departments[j+1]
                departments[j + 1] = temp

                
                temp2 = totals[j]
                totals[j] = totals[j+1]
                totals[j + 1] = temp2

    
    summary = []
    for i in range(len(departments)):
        summary.append((departments[i], totals[i]))

    return summary

def analyze_courses(course_data):
    pop_course = find_most_popular_course(course_data)
    math_list = get_courses_in_department(course_data, "Mathematics")
    summary = get_department_enrollment_summary(course_data)

    return (pop_course, math_list, summary)

course_data = [
    ('CSI01', 'Computer Science', [300, 310, 305]),
    ('MATH201', 'Mathematics', [250, 240, 260]),
    ('ENG101', 'English', [400, 410, 390]),
    ('CS205', 'Computer Science', [280, 290, 300]),
    ('MATH150', 'Mathematics', [350, 360, 340])
]
print(analyze_courses(course_data))
