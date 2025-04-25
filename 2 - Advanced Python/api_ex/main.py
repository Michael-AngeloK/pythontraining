import requests
import json

def fetch_breweries_by_state(state):
    url = f"https://api.openbrewerydb.org/v1/breweries?by_state={state}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        breweries = response.json()
        return breweries
    except requests.exceptions.HTTPError as e:
        return f"HTTP error occurred: {e}"
    except Exception as e:
        return f"Error occurred: {e}"

def fetch_user_data(user_id):
    url = f"https://jsonplaceholder.typicode.com//users/{user_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            "name": data["name"],
            "email": data["email"],
            "address": f"{data["address"]["street"]}, {data["address"]["city"]}",
        }
    except requests.exceptions.HTTPError as e:
        return f"HTTP error occurred: {e}"
    except Exception as e:
        return f"Error occurred: {e}"


def main():
    # state = "texas"
    # breweries = fetch_breweries_by_state(state)
    # print(f"Breweries in {state}")
    # for brewery in breweries:
    #     name = brewery["name"]
    #     type =brewery["brewery_type"]
    #     city = brewery["city"]
    #     print(f"Name: {name}, type: {type}, city:{city}")
    user_id = 1
    user = fetch_user_data(user_id)
    print(user)


if __name__ == "__main__":
    main()