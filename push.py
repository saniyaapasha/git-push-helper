import subprocess
import sys

def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        sys.exit(1)

def push_to_github(commit_message="Update from script", branch="main"):
    run("git add .")
    run(f'git commit -m "{commit_message}"')
    run(f"git push origin {branch}")

if __name__ == "__main__":
    msg = input("Commit message: ") or "Update"
    push_to_github(commit_message=msg)