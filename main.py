import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

class GithubUser:
    def __init__(self, username):
        self.url = f"https://github.com/{username}?tab="

    def get_users(self, user_type):
        response = requests.get(self.url + user_type)
        soup = BeautifulSoup(response.text, 'html.parser')
        return set(elem.text for elem in soup.find_all('span', {'class': 'Link--secondary'}))

    def check_follow_status(self):
        with ThreadPoolExecutor(max_workers=2) as executor:
            followers, followings = executor.map(self.get_users, ['followers', 'following'])

        print("Users not following back:", *(followings - followers), "\nUnique followers:", *(followers - followings), sep='\n')

if __name__ == "__main__":
    GithubUser(input("Enter your username: ")).check_follow_status()
