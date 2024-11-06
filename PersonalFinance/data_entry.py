from datetime import datetime

date_format = "%d-%m-%Y"
#TODO: Expand Categories
CATEGORIES = {"I": "Income", "E": "Expense"}


def get_date(prompt,allow_default=False): #Allow default makes todays date
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)

    #Keep asking for new input till a correct format is given
    try: 
        valid_date = datetime.strptime(date_str, date_format) 
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please use DD-MM-YYYY.")
        return get_date(prompt, allow_default)

#Keeps calling the function until a correct value is given
def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_title():
    title = input("Enter the title: ")
    if not title:
        print("Title cannot be empty.")
        return get_title()
    return title

def get_category():
    category = input("Enter the category (I for Income or E for Expense); ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]

    print("Invalid category. Please enter I 4 income or E 4 Expense.")
    return get_category()

def get_description():
    return input("Enter the description: ")