# Python script to upload or update an HTML file on GitHub using PyGithub

from github import Github
import os

# 1. Install PyGithub:
#    pip install PyGithub

# 2. Set your GitHub personal access token here (create one with repo scope)
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "YOUR_GITHUB_TOKEN")

# 3. Repository details
REPO_NAME = "YourUsername/success-stream"  # format: "owner/repo"
FILE_PATH = "index.html"
COMMIT_MESSAGE = "Upload or update index.html via script"

def upload_file_to_github(token, repo_name, file_path, commit_message):
    """
    Uploads or updates a file in the specified GitHub repository.
    """
    # Authenticate
    g = Github(token)
    repo = g.get_repo(repo_name)
    
    # Read local file content
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    try:
        # Try to get the file from the repo (to update)
        existing_file = repo.get_contents(file_path)
        repo.update_file(
            path=file_path,
            message=commit_message,
            content=content,
            sha=existing_file.sha
        )
        print(f"Updated `{file_path}` successfully.")
    except:
        # If file doesn’t exist, create it
        repo.create_file(
            path=file_path,
            message=commit_message,
            content=content
        )
        print(f"Created `{file_path}` successfully.")

if __name__ == "__main__":
    upload_file_to_github(GITHUB_TOKEN, REPO_NAME, FILE_PATH, COMMIT_MESSAGE)
