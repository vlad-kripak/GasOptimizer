import requests
import time

def get_gas_price():
    url = 'https://ethgasstation.info/api/ethgasAPI.json'
    response = requests.get(url)
    data = response.json()
    # ethgasstation returns gas price * 10
    fastest_gas_gwei = data['fastest'] / 10
    average_gas_gwei = data['average'] / 10
    return fastest_gas_gwei, average_gas_gwei

if __name__ == "__main__":
    while True:
        fastest, average = get_gas_price()
        print(f"Fastest gas price: {fastest} gwei, Average gas price: {average} gwei")
        time.sleep(300)  # update every 5 minutes
