import requests
import os
from dotenv import load_dotenv

# take environment variables from .env.
load_dotenv()

user = os.getenv('GITHUB_USER_NAME')
response = requests.get(f"https://api.github.com/users/{user}/repos")
my_projects = response.json()
print(type(my_projects))
print(len(my_projects))


# print just the names and urls
for project in my_projects:
    print(f"Project Name: {project['name']}\nProject Url: {project['html_url']}\n")
