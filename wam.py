# Grade to GPA mapping (Standard 4.0 Scale)
GRADE_SCALE = {
    "A+": 4.0,  
    "A" : 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B" : 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C" : 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D" : 1.0,
    "E" : 0.0,
    "F" : 0.0,
    "PENDING": None  # Handled distinctly so it doesn't count as a 0.0 fail
}

# Define your institution's weighting for each semester to find the Honorary WAM
# Typically, later years carry heavier weight (e.g., Year 1 = 1, Year 2 = 2 or 3)
SEMESTER_WEIGHTS = {
    "Intake 2023 - Semester 1": 1, 
    "Intake 2023 - Semester 2": 1,
    "Intake 2023 - Semester 3": 2,
    "Intake 2023 - Semester 4": 2,
}

def calculate_gpa(modules):
    """
    Calculates GPA for a list of modules, ignoring pending grades.
    """
    total_credits = 0
    total_honor_points = 0
    
    for mod in modules:
        name = mod.get("name", "Unknown Module")
        credits = mod.get("credits", 0)
        letter_grade = mod.get("grade", "F").upper().strip()
        
        gpa = GRADE_SCALE.get(letter_grade, 0.0)
        
        # If the grade is pending, skip it entirely from calculation
        if letter_grade == "PENDING" or gpa is None:
            print(f"  - {name:<65} | Credits: {credits} | Grade: [PENDING]")
            continue
            
        print(f"  - {name:<65} | Credits: {credits} | Grade: {letter_grade}")
        
        total_credits += credits
        total_honor_points += (gpa * credits)
        
    if total_credits == 0:
        return 0.0, 0
        
    semester_gpa = total_honor_points / total_credits
    return round(semester_gpa, 2), total_credits

def main():
    academic_record = {
        "Intake 2023 - Semester 1": [
            {"name": "Fluid Mechanics", "credits": 2.0, "grade": "B+"},
            {"name": "Programming Fundamentals", "credits": 3.0, "grade": "A"},
            {"name": "Electrical Fundamentals", "credits": 2.0, "grade": "A"},
            {"name": "Mathematics", "credits": 3.0, "grade": "B+"},
            {"name": "Mechanics", "credits": 2.0, "grade": "B-"},
            {"name": "Properties of Materials", "credits": 2.0, "grade": "A"},
        ],
        "Intake 2023 - Semester 2": [
            {"name": "Computer Systems", "credits": 3.0, "grade": "A"},
            {"name": "Theory of Electricity", "credits": 3.0, "grade": "B"},
            {"name": "Communication and Presentation Skills", "credits": 2.0, "grade": "A+"},
            {"name": "Language Skills Enhancement", "credits": 2.0, "grade": "A+"},
            {"name": "Basic Electronics for Engineering Applications", "credits": 3.0, "grade": "A-"},
            {"name": "Methods of Mathematics", "credits": 3.0, "grade": "B"},
            {"name": "Introduction to Manufacturing Processes", "credits": 3.0, "grade": "A"},
        ],
        "Intake 2023 - Semester 3": [
            {"name": "Aspects of Civil Engineering", "credits": 2.0, "grade": "A"},
            {"name": "Power Systems I", "credits": 3.0, "grade": "A-"},
            {"name": "Circuits and Fields", "credits": 3.0, "grade": "A"},
            {"name": "Digital Signal Processing", "credits": 3.0, "grade": "A"},
            {"name": "Engineering Systems Design", "credits": 3.0, "grade": "A"},
            {"name": "Differential Equations", "credits": 2.0, "grade": "A"},
            {"name": "Calculus", "credits": 2.0, "grade": "A"},
            {"name": "Fundamentals of Engineering Thermodynamics and Applications", "credits": 3.0, "grade": "A-"},
        ],
    }
    
    total_wam_credits = 0
    total_wam_points = 0
    
    total_hon_credits_weighted = 0
    total_hon_points_weighted = 0 
    
    print("=" * 90)
    print("                            ENGINEERING PERFORMANCE REPORT                          ")
    print("=" * 90)
    
    for semester, modules in academic_record.items():
        print(f"\n▶ {semester}")
        print("-" * 90)
        
        sem_gpa, sem_credits = calculate_gpa(modules)
        sem_weight = SEMESTER_WEIGHTS.get(semester, 1)
        
        print("-" * 90)
        print(f"  SEMESTER GPA: {sem_gpa:.2f} | Earned Credits: {sem_credits} | (Multiplier Weight: {sem_weight}x)")
        print("-" * 90)
        
        # Standard WAM metrics (Equivalent to uniform cumulative credit-weighted GPA)
        total_wam_credits += sem_credits
        total_wam_points += (sem_gpa * sem_credits)
        
        # Honorary WAM metrics (Applies the academic year/semester level weight multiplier)
        total_hon_credits_weighted += (sem_credits * sem_weight)
        total_hon_points_weighted += (sem_gpa * sem_credits * sem_weight)
        
    print("\n" + "=" * 90)
    if total_wam_credits > 0:
        standard_wam = total_wam_points / total_wam_credits
        honorary_wam = total_hon_points_weighted / total_hon_credits_weighted
        
        print(f" STANDARD WAM / CGPA       : {standard_wam:.2f}")
        print(f" HONORARY WAM              : {honorary_wam:.2f}")
        print(f" TOTAL GRADED CREDITS      : {total_wam_credits}")
    else:
        print(" No academic data available.")
    print("=" * 90)

if __name__ == "__main__":
    main()