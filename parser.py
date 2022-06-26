from logging import error
import requests
from bs4 import BeautifulSoup
from rich.console import Console
from os.path import exists

class Client:
    def __init__(self) -> None:
        self.console = Console()
        self.session = requests.Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0",
            "Accept-Language": "ru"
        }
    
    def load_page(self, page: int = None):
        url = "https://www.wildberries.ru/"
        res = self.session.get(url=url)
        self.console.log(f"res status code: {res.status_code}")
        return res.text
    
    def parse_page(self, text:str):
        soup = BeautifulSoup(text, "lxml")
        # self.console.log(soup.prettify())
        navbar = soup.find_all('li',{"class": "menu-burger__main-list-item j-menu-main-item"})
        # self.console.log(f"navbar: {navbar}")
        
        return [self.parse_item(item) for item in navbar]

    def parse_item(self, item):
        return item.find('a').get_text()

    def run(self):
        if exists("parsed_types.txt"):
            with open("parsed_types.txt", "r") as file: 
                return file.readlines()
        self.console.print("starting parsing")
        try:
            self.console.print("processing")
            parsed_types = self.parse_page(self.load_page())
            with open("parsed_types.txt", 'w') as file:
                for i in parsed_types:
                    file.write(str(i) + "\n")
                file.close()
            self.console.print("completed")
            return parsed_types
        except :
            self.console.log("[bold red] something went wrong")

if __name__ == "__main__":
    client = Client()
    client.run()