import sys

def jamb_checker(jamb_score):
    if float(jamb_score) < 280:
        print("Sorry, your JAMB score does not meet the minimum requirements")
        sys.exit()
    else:
        print("Congrats! Your JAMB score meets the requirements")  

def is_passing_grade(grade):
    return grade.upper() in ['A', 'B', 'C'] 
     
def main():        
    jamb_score = input("Please enter your score in JAMB: ")
    jamb_checker(jamb_score)

    grades = []
    subjects = ["Mathematics", "English", "Physics", "Chemistry", "Biology"]

    for subject in subjects:
        grade = input("Enter grade for {}: ".format(subject))
        grades.append(grade)

    if all(is_passing_grade(grade) for grade in grades):
        print("Congratulations! Your WAEC result met the minimum requirements") 
    else:
        print("Sorry, your WAEC result did not meet the required minimum.")
        sys.exit()

    if float(jamb_score) >= 280 and all(is_passing_grade(grade) for grade in grades):
        print("Congratulations! You meet the requirements to be admitted into the Computer Science department.")
        admitted.append({"JAMB Score": jamb_score, "Grades": grades})
    else:
        print("Sorry, you do not meet the requirements for admission into the Computer Science department.")
        not_admitted.append({"JAMB Score": jamb_score, "Grades": grades})

if __name__ == "__main__":
    admitted = []  # Initialize the admitted list
    not_admitted = []  # Initialize the not_admitted list
    main()  
