# Assignment 3

def calculate_rewards(amount):
    amount = int(amount)
    if amount >= 500:
        return "Gold"
    elif amount > 200:
        return "Silver"
    elif amount > 100:
        return "Bronze"
    else:
        return "None"

def process_customer_data(file):
    customers_dict = {}
    with open(file, "r") as file:
        for line in file:
            name, amount_spent = line.strip().split(',')
            customers_dict[name] = (amount_spent, calculate_rewards(amount_spent))
    return customers_dict

# customers = {}
# with open("customers.txt", "r") as file:
#     for line in file:
#         name, amount_spent = line.strip().split(',')
#         customers[name] = amount_spent



# customers_dict = {}
# for name, amount_spent in customers.items():
#     customers_dict[name] = (amount_spent, calculate_rewards(amount_spent))
#
# print(customers_dict)

print(process_customer_data("customers.txt"))