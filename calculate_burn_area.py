def calculate_burn_area(age, weight):
    if age < 1 or age > 100:
        raise ValueError("Age should be between 1 and 100.")

    if weight <= 0:
        raise ValueError("Weight should be greater than zero.")

    # Rule of Nines percentages for different body parts
    rule_of_nines = {
        "head": 9,
        "arms": 9,
        "chest": 18,
        "abdomen": 18,
        "back": 18,
        "groin": 1,
        "legs": 18
    }

    total_body_surface_area = rule_of_nines["head"] + rule_of_nines["arms"] + \
        rule_of_nines["chest"] + rule_of_nines["abdomen"] + rule_of_nines["back"] + \
        rule_of_nines["groin"] + rule_of_nines["legs"]

    burn_percentage = (age / 9) * (weight / total_body_surface_area)

    return burn_percentage


# Example usage
age = int(input("Enter the patient's age: "))
weight = float(input("Enter the patient's weight (in kg): "))

burn_percentage = calculate_burn_area(age, weight)
print(f"The estimated burn area is {burn_percentage:.2f}%.")
