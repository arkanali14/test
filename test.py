def calculate_grade():
    """"""
    try:
        grade = float(input("Enter the student's grade: "))

        if grade >= 90:
            evaluation = "Excellent"
        elif grade >= 80:
            evaluation = "Very Good"
        elif grade >= 70:
            evaluation = "Good"
        elif grade >= 60:
            evaluation = "Acceptable"
        else:
            evaluation = "Fail"

        print("Evaluation:", evaluation)

    except ValueError:
        print("Error: Please enter a valid number for the grade.")

# Call the function to run the program
calculate_grade()
