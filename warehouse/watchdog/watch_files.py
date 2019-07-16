import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


project = "test_warehouse"


def get_keys(path):
    keys = path.split("/")
    pidx =  keys.index(project)
    keys = keys[pidx:]

    return keys


class Watcher:
    DIRECTORY_TO_WATCH = "../{}/".format(project)

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            fpath = event.src_path
            keys = get_keys(fpath)

            if keys[-1] != "end":
                print("Received created event - {}.".format(keys))
            else:
                # sys.exit()
                subprocess.call(['python', './kill.py'])



if __name__ == '__main__':
    w = Watcher()
    w.run()