def _get_number(index):
    number = float(input(f"Number {index}: "))
    return number


def _get_goal():
    print("""
    Options:
    - "add"
    - "subtract"
    - "multiply"
    - "divide"
    - "check factors"
    """)
    user_input = input("What would you like to do with these numbers?:  ")
    return user_input

_get_goal()