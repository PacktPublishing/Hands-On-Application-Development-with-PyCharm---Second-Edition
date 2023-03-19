computer_science_grades = {
    "Guido van Rossum": 100,
    "Ewa Jodlwska": 99,
    "Fabrizio Romano": 88,
    "Henrich Kruger": 87,
    "Rick van Hattem": 83,
    "Steven Lott": 72,
    "Dusty Phillips": 72,
    "Quan Nguyen": 92
}


advanced_theoretical_and_applied_recess_grades = {
    "Bruce Van Horn": 100,
    "Prajakta Naik": 92,
    "Kinnari Chohan": 88,
    "Pooja Yadiv": 86
}


def computer_science_average(grades: dict) -> float:
    raw_total = 0
    for grade in grades.values():
        raw_total += grade

    average = (raw_total / len(grades))
    return average


def advanced_recess_average(grades: dict) -> float:
    raw_total = 0
    for grade in grades.values():
        raw_total += grade

    average = (raw_total / len(grades))
    return average


boring_class_average = computer_science_average(computer_science_grades)
print(f"Boring average is {boring_class_average}")

popular_kid_average = \
    advanced_recess_average(advanced_theoretical_and_applied_recess_grades)
print(f"Popular average is {popular_kid_average}")
