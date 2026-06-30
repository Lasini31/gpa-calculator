# Grade to GPA mapping (Standard 4.0 Scale)
# Adjust these values to match your university's specific handbook if needed
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
    "Pending" : 0.0
}

def calculate_gpa(modules):
    """
    Calculates GPA for a list of modules and prints individual breakdown.
    """
    total_credits = 0
    total_honor_points = 0
    
    for mod in modules:
        name = mod.get("name", "Unknown Module")
        credits = mod.get("credits", 0)
        letter_grade = mod.get("grade", "F").upper().strip()
        
        # Look up the GPA from our scale
        gpa = GRADE_SCALE.get(letter_grade, 0.0)
        
        # Print module details for clear visibility
        print(f"  - {name:<35} | Credits: {credits} | Grade: {letter_grade}")
        
        total_credits += credits
        total_honor_points += (gpa * credits)
        
    if total_credits == 0:
        return 0.0, 0
        
    semester_gpa = total_honor_points / total_credits
    return round(semester_gpa, 2), total_credits

def main():
    # Academic record including Module Names
    academic_record = {
        # Academic record from your engineering transcripts
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
        "Intake 2023 - Semester 4": [
            {"name": "Modular Software Development", "credits": 3.0, "grade": "Pending"},
            {"name": "Electrical Machines in Power Systems", "credits": 3.0, "grade": "Pending"},
            {"name": "Electrical Measurements and Instrumentation", "credits": 3.0, "grade": "Pending"},
            {"name": "Control Systems", "credits": 3.0, "grade": "Pending"},
            {"name": "Electrical Installations", "credits": 3.0, "grade": "Pending"},
            {"name": "Technical Report Writing for Engineering Studies", "credits": 3.0, "grade": "A+"},
            {"name": "Applied Statistics", "credits": 2.0, "grade": "Pending"},
            {"name": "Numerical Methods", "credits": 2.0, "grade": "Pending"},
        ],
    }
    
    overall_total_credits = 0
    overall_honor_points = 0 
    
    print("=" * 60)
    print("                      ACADEMIC PERFORMANCE REPORT          ")
    print("=" * 60)
    
    for semester, modules in academic_record.items():
        print(f"\n▶ {semester}")
        print("-" * 60)
        
        sem_gpa, sem_credits = calculate_gpa(modules)
        
        print("-" * 60)
        print(f"  SEMESTER GPA: {sem_gpa:.2f} | Total Semester Credits: {sem_credits}")
        print("-" * 60)
        
        overall_total_credits += sem_credits
        overall_honor_points += (sem_gpa * sem_credits)
        
    print("\n" + "=" * 60)
    if overall_total_credits > 0:
        cumulative_gpa = overall_honor_points / overall_total_credits
        print(f" FINAL CUMULATIVE GPA (CGPA) : {cumulative_gpa:.2f}")
        print(f" TOTAL EARNED CREDITS        : {overall_total_credits}")
    else:
        print(" No academic data available.")
    print("=" * 60)

if __name__ == "__main__":
    main()