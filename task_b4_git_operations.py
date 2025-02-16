from git import Repo
import os
from task_b1_restrict_access import safe_path


def clone_and_commit(repo_url, commit_message):
    repo_path = safe_path("repo_clone")
    if not os.path.exists(repo_path):
        Repo.clone_from(repo_url, repo_path)

    repo = Repo(repo_path)
    with open(os.path.join(repo_path, "new_file.txt"), 'w') as f:
        f.write("Automated commit")

    repo.git.add(all=True)
    repo.index.commit(commit_message)
    repo.remote().push()

    print("Commit pushed successfully!")
