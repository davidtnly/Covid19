import os
import shutil
import time

login_name = os.getlogin()
now = time.ctime(time.time())

# Move to directory with csv files to merge
os.chdir("Merge")

# Directories
merge_path = os.getcwd()
new_files_path = 'C:\\Users\\' + login_name + '\\Documents\\Programming\\COVID-19\\csse_covid_19_data\\csse_covid_19_daily_reports\\'

# Files
merge_files = os.listdir(merge_path)
files = [os.path.join(merge_path, filename) for filename in merge_files]

# Get max file date
file_dates = []

for filename in files:
    print((os.path.getmtime(filename)))
    file_dates.append((os.path.getmtime(filename)))

old_file_date = max(file_dates)


# Remove old files
os.chdir(merge_path)
os.listdir()

for filename in files:
#     print("Last modified: %s" % time.ctime(os.path.getmtime(filename)))
    if (os.path.getmtime(filename)) > old_file_date:
        print('New file found: ', filename)
    else:
        print('Not new. Proceeding to remove.')
        os.remove(filename)

# Add new files
os.chdir(new_files_path)
covid_folder = os.getcwd()
covid_folder_files = os.listdir(covid_folder)
covid_files = [os.path.join(covid_folder, filename) for filename in covid_folder_files]

for filename in covid_files:
    if (os.path.getmtime(filename)) > old_file_date and filename.endswith('.csv'):
        print('Found new file updated on', time.ctime(os.path.getmtime(filename)), ': \n', filename)
        print('Adding file to merge folder...')
        shutil.copyfile(filename, os.path.join(merge_path, os.path.basename(filename)))