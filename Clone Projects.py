import os
import subprocess

# List of GitHub repo URLs
repos = [
    "https://github.com/pallets/flask.git",
    "https://github.com/django/django.git",
    "https://github.com/psf/requests.git",
    "https://github.com/pandas-dev/pandas.git",
    "https://github.com/numpy/numpy.git",
    "https://github.com/scikit-learn/scikit-learn.git",
    "https://github.com/matplotlib/matplotlib.git",
    "https://github.com/wention/BeautifulSoup4.git"
]

base_dir = "python_projects"

os.makedirs(base_dir, exist_ok=True)

for repo in repos:
    repo_name = repo.split("/")[-1].replace(".git", "")
    repo_path = os.path.join(base_dir, repo_name)
    
    if not os.path.exists(repo_path):
        print(f"Cloning {repo_name}...")
        subprocess.run(["git", "clone", repo, repo_path])
    else:
        print(f"{repo_name} already exists, skipping...")
