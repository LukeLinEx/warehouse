import os

kill_cmd = "kill $(ps -e | grep python\ watch_files.py | awk '{print $1}')"


if __name__ == "__main__":
    os.system(kill_cmd)
