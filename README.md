# Github Followers Checker

![Visitors](https://badges.pufler.dev/visits/IRedDragonICY/Github_Followers_Checker)
![Python Version](https://img.shields.io/badge/python-3.x-blue.svg) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Stars](https://img.shields.io/github/stars/IRedDragonICY/Github_Followers_Checker?style=social)

## Description
This Python script is designed to check the follow status of a GitHub user. It can tell you which users are not following you back and who are your unique followers.

## Dependencies
- Python 3.x
- requests
- BeautifulSoup
- concurrent.futures

## Installation
First, clone this repository to your local machine using `https://github.com/IRedDragonICY/Github_Followers_Checker.git`.

Next, navigate to the cloned repository's directory.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the necessary Python packages.

```bash
pip install requests
pip install beautifulsoup4
```

## Usage
Run the script using Python.

```bash
python GithubUserFollowStatusChecker.py
```

When prompted, enter your GitHub username.

The script will output the users who are not following you back and your unique followers.

## Code Structure
The script contains a class `GithubUser` which has the following methods:

- `__init__(self, username)`: Initializes the GithubUser object with the given username.

- `get_users(self, user_type)`: Fetches the followers or following users of the current GithubUser.

- `check_follow_status(self)`: Checks which users the current GithubUser is following but are not following back and who are the unique followers of the current GithubUser.

The script uses a ThreadPoolExecutor to fetch the followers and following users concurrently to speed up the process.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
