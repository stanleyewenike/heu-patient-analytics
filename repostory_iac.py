from github import Github
import os

# It's better to use environment variables for sensitive information like tokens
github_token = os.getenv("GITHUB_TOKEN")
repo_name = "NHS-Health-Analytics"
description = "Repository for NHS HEU Data Science Project"

if not github_token:
    raise ValueError("Please set the GITHUB_TOKEN environment variable")

try:
    g = Github(github_token)
    user = g.get_user()
    org = g.get_organization(user.login)
    repo = org.create_repo(repo_name, description=description, private=True)

    # Create essential directories and files
    structure = {
        "data": ["raw", "processed"],
        "notebooks": ["EDA", "modeling"],
        "scripts": ["etl", "visualization", "modeling"],
        "docs": []
    }

    for folder, subfolders in structure.items():
        repo.create_file(f"{folder}/.gitkeep", "Initial commit", "")
        for sub in subfolders:
            repo.create_file(f"{folder}/{sub}/.gitkeep", "Initial commit", "")

    print(f"Repository {repo_name} created successfully!")

except Exception as e:
    print(f"An error occurred: {e}")