import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.example.com"

    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    print("Title:", soup.title.text)

if __name__ == "__main__":
    main()