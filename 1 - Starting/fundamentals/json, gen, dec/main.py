import json

def cache_decorator(func):
    cache = {}
    def wrapper(*args, **kwargs):
        if args[0] in cache:
            print(f"Cache found {args[0]}")
            return cache[args[0]]
        else:
            print(f"API Call for {args[0]}")
            result = func(args[0])
            cache[args[0]] = result
            return result
    return wrapper

@cache_decorator
def get_company_name(ticker):
    """Simulated API function to fetch a company name based on the ticker symbol."""
    # Simulate different responses based on the ticker symbol
    api_responses = {
        "AAPL": "Apple Inc.",
        "MSFT": "Microsoft Corporation",
        "GOOGL": "Alphabet Inc."
    }
    return api_responses.get(ticker, "Unknown Company")


def read_and_filter_temperatures(filename, threshold):
    try:
        with open(filename, "r") as file:
            for line in file:
                words = line.strip().split(",")
                temp = float(words[1])
                if temp > threshold:
                    yield temp
    except FileNotFoundError:
        raise Exception(f"File '{filename}' not found")



def main():
    with open("sales_data.json", "r") as file:
        data = json.load(file)
    print(json.dumps(data, sort_keys=True, indent=2))

    sales_per_category = {}
    for item in data:
        category = item['category']
        total_sales = item['price_per_unit'] * item['quantity']
        if category in sales_per_category:
            sales_per_category[category] += total_sales
        else:
            sales_per_category[category] = 0

    aggregated_sales = [{"category": key, "total_sales": value} for key, value in sales_per_category.items()]
    with open("aggregated_sales.json", "w") as file:
        json.dump(aggregated_sales, file, indent=4)

    filtered_temperatures = read_and_filter_temperatures("sensor_data.txt", 12)

    print("Filtered temperatures:")
    for temp in filtered_temperatures:
        print(f"{temp}")

    # Test the decorated function
    print(get_company_name("AAPL"))  # Expected to trigger an API call
    print(get_company_name("AAPL"))  # Expected to use cached data
    print(get_company_name("MSFT"))  # Expected to trigger an API call
    print(get_company_name("MSFT"))  # Expected to use cached data
    print(get_company_name("GOOGL"))  # Expected to trigger an API call
    print(get_company_name("GOOGL"))  # Expected to use cached data

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Exception occurred: {e}")