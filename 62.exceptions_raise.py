def calculate_age(age):
    if (age <= 0):
        raise ValueError("age cannot be zero or less")
    return 10 / age


try:
    calculate_age(10)
except ValueError as err:
    print(err)
