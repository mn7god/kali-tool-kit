import os

def root():
  rootcheck = os.geteuid()
  if rootcheck == 0:
    with open('kali-full.txt', 'r') as file:
      for line in file.readlines():
        print(f"installing {line}...")
        os.system(f"sudo apt install {line} -y")
  else:
    print("you need\033[0;91m root\033[0m to continue")
      
root()
