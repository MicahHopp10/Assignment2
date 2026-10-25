"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    num = annual_cost / SEMESTERS_PER_YEAR
    return num


def cost_per_month(annual_cost):
    num = annual_cost / MONTHS_PER_YEAR
    return num


def cost_per_day(annual_cost):
    num = annual_cost / (CLASS_DAYS_PER_SEMESTER * 2)
    return num


def cost_per_credit(annual_cost, credits):
    num = annual_cost / (credits * 2)
    return num


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    num = annual_cost / (credits / CS1430_CREDITS * CS1430_MEETINGS_PER_SEMESTER * SEMESTERS_PER_YEAR)
    return num

def cost_per_minute(annual_cost, credits):
    num = (annual_cost / (credits / CS1430_CREDITS * CS1430_MEETINGS_PER_SEMESTER * SEMESTERS_PER_YEAR)) / 50
    return num


# ---- PROGRAM ----

def main():
    yearly_cost = float(input("Total cost for one year? "))
    semester_credits = float(input("How many credits this semester? "))
    minutes_late = float(input("Minutes late? "))

    while True:
        print("Cost of College :-]")
        print("1. Per Semester")
        print("2. Per Month")
        print("3. Per Day")
        print("4. Per Credit")
        print("5. Per Class")
        print("6. Per Minute Late")
        print("Q. Quit")

        choice = input("Choose an option: ")

        if choice == "Q":
            break
        elif choice == '1':
            print(f"One Semester Costs ${cost_per_semester(yearly_cost):.2f}")
        
        elif choice == '2':
            print(f"One Month Costs ${cost_per_month(yearly_cost):.2f}")

        elif choice == '3':
            print(f"One Day Costs ${cost_per_day(yearly_cost):.2f}")

        elif choice == '4':
            print(f"One Credit Costs ${cost_per_credit(yearly_cost, semester_credits):.2f}")

        elif choice == '5':
            print(f"One CS1430 Class Costs ${cost_per_class(yearly_cost, semester_credits):.2f}")

        elif choice == '6':
            print(f"Being {minutes_late} minutes late costed you ${cost_per_minute(yearly_cost, semester_credits):.2f}")

        elif choice == 'q':
            print("Try Q Next Time, Learn to Read Dum Dum")
        
        else:
            print("Not a Valid Option Dum Dum")
            


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
