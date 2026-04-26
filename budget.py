# PACKAGES
from enum import Enum

# ENUM CLASSES
''' 
Enum stands for "enumeration", which means that it gives me a list of pre-approved options to choose from in a specified category

the way I'm using it in the code below means that each time I create a class, I can make it so that any instance (aka the characteristics of the class, like frequency, value, etc) can be set to one of the Enum classes that I've created.
When I do this, that means each entry for that specific instance will need to be one of the options in that Enum class.
'''
class Frequency(Enum):
    ANNUAL = "annual"
    MONTHLY = "monthly"
    WEEKLY = "weekly"
    DAILY = "daily"
    ONE_TIME = "one time"

    # when any Enum member is printed, it will show as its value instead of itself
    def __str__(self):
        return self.value

class Category(Enum):
    HOUSING = "housing"
    UTILITIES = "utilities"
    MEDICAL = "medical"
    TRANSPORT = "transport"
    GROCERIES = "groceries"
    ENTERTAINMENT = "entertainment"
    SUBSCRIPTION = "subscription"
    SAVINGS = "savings"
    MISC = "miscellaneous"

    def __str__(self):
        return self.value

class Source(Enum):
    LAURA = "Laura"
    IAN = "Ian"
    INTEREST = "Interest"

    def __str__(self):
        return self.value

# CLASSES
class Expense:
    # this creates a list that all Expense objects will be appended to when created
    all_expenses = []
    
    def __init__(self, value, frequency: Frequency, category: Category):
        if not isinstance(frequency, Frequency):
            raise ValueError("Enter a valid frequency.")
        if not isinstance(category, Category):
            raise ValueError("Enter a valid category.")
        self.value = value
        self.frequency = frequency
        self.category = category
        Expense.all_expenses.append(self)

class Income:
    all_incomes = []
    
    def __init__(self, value, source: Source):
        if not isinstance(source, Source):
            raise ValueError("Enter a valid source.")
        self.value = value
        self.source = source
        Income.all_incomes.append(self)
    
    # this creates a class method that sums up all entries with class Income
    @classmethod
    def total_income(cls):
        total= sum(income.value for income in Income.all_incomes)
        return total

# ENTRIES
hls_income = Income(3690, Source.LAURA)
globallogic_income = Income(2352, Source.IAN)
total_income = Income.total_income()
print(total_income)

monthly_rent = Expense(2325, Frequency.MONTHLY, Category.HOUSING)
monthly_utilities = Expense(200, Frequency.MONTHLY, Category.UTILITIES)
monthly_savings = Expense(total_income*0.2, Frequency.MONTHLY, Category.SAVINGS)



# monthly_budget = total_monthly - monthly_expenses
# weekly_budget = monthly_budget/4

# print("Monthly Budget: " + str(monthly_budget))
# print("Weekly Budget: " + str(weekly_budget))
