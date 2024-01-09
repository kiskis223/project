from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler
class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_track):
            extension = filename.split(".")
            if len(extension) > 1 and (extension[1].lower() == "jpg" or extension[1].lower() == "png"):
                file = folder_track + "/" + filename
                new_patch = folder_dest + "/" + filename
                os.rename(file, new_patch)


folder_track = 'C:/Users/ZXC/Pictures/телега'
folder_dest = 'C:/Users/ZXC/Pictures/folder'

handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()

try:
    while(True):
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()