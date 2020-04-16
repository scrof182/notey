#!/usr/bin/python3
import os

## CHANGE_ME this is the directory where your notes are stored
working_dir = "/Users/mselph/testing_notes"

# git variables
git_add = "git add *"
git_commit = 'git commit -m "daily update"'
git_push = "git branch --show-current | xargs git push -u origin"

# git commands
os.chdir(working_dir)
os.system(git_add)
os.system(git_commit)
os.system(git_push)