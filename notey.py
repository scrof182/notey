#!/usr/bin/python3
import os
from datetime import datetime
import argparse

## CHANGE_ME this is the directory where your notes are stored
working_dir = "/full/path/to/dir"
os.chdir(working_dir)

##CHANGE_ME These are the high level folders that need to be created; modify if you want other folders created
folders = ["daily_notes", "incidents", "projects", "training"]

## Parsers set up
parser = argparse.ArgumentParser(description='Notey Script for all things Note Related')
g = parser.add_mutually_exclusive_group()
g.add_argument('-f', '--first', help='First Setup for Notey', action='store_true')
g.add_argument('-s', '--start_of_day', help='Used to create a new daily notes file from daily notes template', action='store_true')
g.add_argument('-n', '--new_folder', help='Used to create a new high level folder')
g.add_argument('-e', '--end_of_day', help='Perform a git push to remote repo', action='store_true')
g.add_argument('-a', '--allmark', help='Restart Allmark', action='store_true')
args = parser.parse_args()

## grab current time and setup path variables 
now = datetime.now()
year = f"{now.year:04d}"
month = f"{now.month:02d}"
day = f"{now.day:02d}"
hour = f"{now.hour:02d}"
minute = f"{now.minute:02d}"
second = f"{now.second:02d}"
month_spelled = now.strftime("%B")

# build header and paths
daily_header = "# " + month_spelled + " " + day + " " + year 
year_path = "daily_notes/" + year
month_path = year_path + "/" + month
day_path = month_path + "/" + day 
day_file = day_path + "/" + day + ".md"

def create_daily_notes_file():
	year_exist = os.path.isdir(year_path)
	month_exist = os.path.isdir(month_path)
	day_exist = os.path.isfile(day_path)
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

def create_notes_template_file():
	notes_template = "echo '\n## Stuff on tap \n\n## Done Stuff' >> daily_notes/notes_template.md"
	os.system("touch daily_notes/notes_template.md")
	os.system(notes_template)

def create_inital_folders():
	for item in folders:
		cmd = "mkdir " + item
		os.system(cmd)

def kill_and_restart_allmark():
	allmark_kill = "docker rm -f allmark"
	allmark_pull = "docker pull andreaskoch/allmark"
	allmark_start = "docker run -dit --name allmark  -v $(pwd):/data -p 8888:33001 andreaskoch/allmark"
	os.system(allmark_kill)
	os.system(allmark_pull)
	os.system(allmark_start)

def clone_changes_to_repo():
	git_add = "git add *"
	git_commit = 'git commit -m "daily update"'
	git_push = "git branch --show-current | xargs git push -u origin"
	os.chdir(working_dir)
	os.system(git_add)
	os.system(git_commit)
	os.system(git_push)

def pull_changes_to_repo():
	checkout_master = "git checkout master"
	pull = "git pull"
	os.system(checkout_master)
	os.system(pull)

if args.first == True:
	create_inital_folders()
	create_notes_template_file()
	create_daily_notes_file()
	kill_and_restart_allmark()

if args.start_of_day == True:
	pull_changes_to_repo()
	create_daily_notes_file()
	kill_and_restart_allmark()

if args.end_of_day == True:
	clone_changes_to_repo()

if args.allmark == True:
	kill_and_restart_allmark()

if args.new_folder != None and len(args.new_folder) > 0:
	cmd = "mkdir " + args.new_folder
	os.system(cmd)