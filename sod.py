#!/usr/bin/python3
import os
from datetime import datetime

## CHANGE_ME this is the directory where your notes are stored
working_dir = "/full/path/to/working/dir"
os.chdir(working_dir)

## grab current time and setup branch and path variables 
# current time
now = datetime.now()

# strings for all the different formats
year = f"{now.year:04d}"
month = f"{now.month:02d}"
day = f"{now.day:02d}"
hour = f"{now.hour:02d}"
minute = f"{now.minute:02d}"
second = f"{now.second:02d}"
month_spelled = now.strftime("%B")

# build headers and paths
daily_header = "# " + month_spelled + " " + day + " " + year 
year_path = "daily_notes/" + year
month_path = year_path + "/" + month
day_path = month_path + "/" + day 
day_file = day_path + "/" + day + ".md"

## Git commands and env set up 
# build git commands
checkout_master = "git checkout master"
pull = "git pull"
# new_branch = "git checkout -b " + branch

# create new git branch
os.system(checkout_master)
os.system(pull)
#os.system(new_branch)

## Create today's notes folder
year_exist = os.path.isdir(year_path)
month_exist = os.path.isdir(month_path)
day_exist = os.path.isdir(day_path)
day_file_exist = os.path.isfile(day_file)

if year_exist == False:
	cmd = "mkdir " + year_path
	os.system(cmd)

if month_exist == False:
	cmd = "mkdir " + month_path
	os.system(cmd)

if day_exist == False:
	cmd = "mkdir " + day_path
	os.system(cmd)

if day_file_exist == False:
	touch_file = "touch " + day_file
	insert_header = "echo '" + daily_header + "' >> " + day_file
	copy_template = "cat daily_notes/notes_template.md >> " + day_file
	os.system(touch_file)
	os.system(insert_header)
	os.system(copy_template)

## Pull down markdown viewer and start it
allmark_kill = "docker rm -f allmark"
allmark_pull = "docker pull andreaskoch/allmark"
allmark_start = "docker run -dit --name allmark  -v $(pwd):/data -p 8888:33001 andreaskoch/allmark"
os.system(allmark_kill)
os.system(allmark_pull)
os.system(allmark_start)