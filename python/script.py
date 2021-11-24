import os
import sys

directory = "../"
cwd = os.getcwd()
print("Current directory is: " + cwd)
print("=================================================================")
print("These files have been changed: ")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory = sys.argv[1]

bash_command = ["cd " + directory, "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False

for result in result_os.split('\n'):
    if result.find('\t') != -1:
        print(result)
