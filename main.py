import requests
import json
import argparse
 
API_URL = "https://www.travel-advisory.info/api"
 
def fetch_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        with open("data.json", "w") as file:
            json.dump(data, file)
    else:
        print("Failed to fetch data from the API")
 
def lookup_country(country_code):
        with open("data.json", "r") as file:
            data = json.load(file)
            country_name = data["data"][country_code]["name"]
            return country_name
 
def main():
    parser = argparse.ArgumentParser(description="Country Lookup Tool")
    parser.add_argument("--countrycode", nargs="+", help="Country code(s) for lookup")

 
    args = parser.parse_args()

    if args.countrycode:
        for country_code in args.countrycode:
            country_name = lookup_country(country_code)
            print(f"{country_code}: {country_name}")
 
if __name__ == "__main__":
    main()