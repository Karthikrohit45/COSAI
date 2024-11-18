def check_voting_eligibility(age):
    if age>= 18:
        print("You are eligible for voting")
    else:
        print("You are not eligible for voting")
try:
    num = int(input("Enter Age:"))

    check_voting_eligibility(num)
except ValueError:
    print("Invalid input! Please enter a valid input.")
