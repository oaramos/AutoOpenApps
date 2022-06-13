import os
import psutil

for p in psutil.process_iter(['status']):
    if p.info['status'] == psutil.STATUS_RUNNING and p.name() == 'Google Chrome':
        os.system("""osascript -e 'tell app "Messages" to open'""")


# if google_chrome_open == True:
#   os.system("""osascript -e 'tell app "Messages" to open'""")


# run find_procs_by_name to see current status of app
# check if app status='running'
# if app status='running', use os.system to open another app
