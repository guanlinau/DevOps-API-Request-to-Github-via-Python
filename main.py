import requests
import os
from dotenv import load_dotenv

# take environment variables from .env.
load_dotenv()

response = requests.get('https://api.github.com/user/repos', auth=(os.getenv("GITHUB_USER_NAME"), os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")))
my_projects = response.json()


for project in my_projects:
  print(f"Project Name: {project['name']}\nProject URL: {project['html_url']}\n")
