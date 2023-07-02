def calculate_ldl_cholesterol(total_cholesterol, triglycerides, hdl_cholesterol):
    if total_cholesterol <= 0 or triglycerides <= 0 or hdl_cholesterol <= 0:
        raise ValueError("All values should be greater than zero.")

    # Calculate LDL cholesterol using the Friedewald equation
    ldl_cholesterol = total_cholesterol - (hdl_cholesterol +
                                           (triglycerides / 5))

    return ldl_cholesterol


# Example usage
total_cholesterol = float(input("Enter the total cholesterol level (mg/dL): "))
triglycerides = float(input("Enter the triglycerides level (mg/dL): "))
hdl_cholesterol = float(input("Enter the HDL cholesterol level (mg/dL): "))

ldl_cholesterol = calculate_ldl_cholesterol(total_cholesterol, triglycerides, hdl_cholesterol)
print(f"The estimated LDL cholesterol level is {ldl_cholesterol:.2f} mg/dL.")
