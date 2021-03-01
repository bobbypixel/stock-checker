import random
import requests

API_URL = "https://cloud.iexapis.com/stable/stock/[STOCK-SYMBOL]/quote"

catchphrases = [
    "I LIKE THE STOCK! 🦍🚀💎🙌",
    "I AM NOT A CAT! 🐱🐱🐱",
    "TO THE MOON 🚀🚀🚀",
    "APES STRONG TOGETHER 🦍🦍🦍",
]


def get_stock_price(api_token, symbol: str) -> str:
    url = API_URL.replace("[STOCK-SYMBOL]", symbol)
    response = requests.get(
        url,
        params={"token": api_token},
    )
    if response.status_code == 200:
        latest_price = response.json()["latestPrice"]
        return (
            f"\nTHE LATEST PRICE IS ${latest_price}.\n{random.choice(catchphrases)}\n"
        )
    else:
        return f"\nBruh, I can't find the stock.\n"


def get_choice(prompt):
    return input(prompt).upper()


def start():
    api_prompt = (
        "💎🙌 A SIMPLE STOCK PRICE CHECKER 🙌💎\nENTER YOUR IEXCLOUD.IO API TOKEN: "
    )

    api_token = input(api_prompt)

    prompt = "\nENTER A STOCK SYMBOL TO SEE ITS LATEST PRICE (OR ENTER Q TO QUIT): "

    choice = get_choice(prompt)
    while choice != "Q":
        print(get_stock_price(api_token, choice))
        choice = get_choice(prompt)


if __name__ == "__main__":
    start()
