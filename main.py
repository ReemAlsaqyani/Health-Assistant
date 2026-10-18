import math

def main():
    print("Welcome to your Health Assistant!")
    print("--------------------------------")

    try:
        while True:
            age = int(input("Enter your age: "))
            if age > 0:
                break
            print("Invalid age! Please enter a positive number.")

        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))

        bmi = weight / math.pow(height, 2)
        print("Your BMI is:", round(bmi, 2))

        if bmi < 18.5:
            status = "Underweight"
        elif bmi < 25:
            status = "Normal weight"
        elif bmi < 30:
            status = "Overweight"
        else:
            status = "Obese"

        print("Status:", status)

        gender = input("Enter your gender (m/f): ")

        height_cm = height * 100

        if gender == "m":
            calories = (10 * weight) + (6.25 * height_cm) - (5 * age) + 5

        elif gender == "f":
            calories = (10 * weight) + (6.25 * height_cm) - (5 * age) - 161

        else:
            print("Please enter m or f only!")
            return

        print("Daily Calorie Needs (BMR):", round(calories), "kcal")
        print("--------------------------------")


        water_cups = int(input("How many cups of water do you usually drink per day? "))

        if water_cups < 8:
            print("Advice: You need to drink more water.")

        elif 8 <= water_cups <= 12:
            print("Advice: Great! You are a healthy person.")

        else:
            print("Advice: Drinking more than 12 cups might be unhealthy.")

    except ValueError:
        print("Error: Please enter numbers only!")

main()