def calculate_atr(years_of_experience, age):
    if years_of_experience > 25 and age >= 55:
        return 5600000
    elif years_of_experience > 20 and age >= 45:
        return 4480000
    elif years_of_experience > 10 and age >= 35:
        return 1500000
    else:
        return 550000

def main():
    years_of_experience = int(input("Enter years of experience: "))
    age = int(input("Enter age: "))

    atr = calculate_atr(years_of_experience, age)
    print("Annual Tax Revenue (ATR): N", atr)

if __name__ == "__main__":
    main()
