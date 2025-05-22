sex = input("Enter your sex (Male/Female): ").lower().strip()

while sex not in ['male', 'female']:
    print("Invalid sex. Please enter 'Male' or 'Female'.")
    sex = input("Enter your sex (Male/Female): ").lower().strip()


def calculate(weight_, height_, age_):
    if sex == 'male':
        print(f'Your BMR (Basal Metabolic Rate) is: {10 * weight_ + 6.25 * height_ - 5 * age_ + 5}')
    else:
        print(f'Your BMR (Basal Metabolic Rate) is: {10 * weight_ + 6.25 * height_ - 5 * age_ - 161}')


while True:
    try:
        age = input("Enter your age: ").strip()
        age = int(age)
        break
    except ValueError:
        print("Invalid age. Please enter a number.")


while True:
    try:
        height = input("Enter your height in centimeters (e.g., 175cm): ")
        height = height.replace('cm', '').lower().strip()
        height = int(height)
        break
    except ValueError:
        print("Invalid height. Please enter numbers only.")


while True:
    try:
        weight = input("Enter your weight in kg (e.g., 70kg): ")
        weight = weight.replace('kg', '').lower().strip()
        weight = int(weight)
        break
    except (TypeError, ValueError):
        print("Invalid weight. Please enter numbers only.")

calculate(weight, height, age)