# Notey

## Summary 

Notey was developed to be way for me to manage my notes using AllMark, markdown, sublime, and git.

AllMark GitHub: https://github.com/andreaskoch/allmark
AllMark Docker: https://hub.docker.com/r/andreaskoch/allmark/

## Prerequisites
  * OSX (Linux might work too, but it's not tested)
  * Docker installed 
  	* https://docs.docker.com/docker-for-mac/install/
  * Git installed and configured
    * https://gist.github.com/derhuerst/1b15ff4652a867391f03
    * https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
  * Your favorite text editor; I use Sublime but Atom is also super great
    * I recommend adding this line to your sublime preferences `"save_on_focus_lost": true`

## Usage

'-f', '--first', help='First Setup for Notey'

'-s', '--start_of_day', help='Used to create a new daily notes file from daily notes template'

'-n', '--new_folder', help='Used to create a new high level folder'

'-e', '--end_of_day', help='Perform a git push to remote repo', action='store_true'

'-a', '--allmark', help='Restart Allmark'

### Initial Setup
  * Create a private git repo
    * https://help.github.com/en/enterprise/2.13/user/articles/creating-a-new-repository
  * Clone the repo to the folder you want your notes stored in via 
    * `git clone $repo.git`
  * Change the `working_dir` variable in notey.py to the folder where the .git file is located
  * Review and customize the list of top level folders to your needs by editing the `folders` variable
  * make python scripts executable via
    * `chmod +x notey.py`
  * run initial_run.py via `./notey.py -f`
  * This will create all necessary directories and file paths
  * Open directory in Sublime and edit files to your hearts content
  * Navigate to http://localhost:8888 in order to view your files in AllMark

### Daily Usage
  * Run `notey.py -s` to create a new daily notes file in the correct directory
  * This notes file will be populated with a template you can modify
  * Open a web browser and navigate to http://localhost:8888 to view your notes in markdown
  * When you want to save your work, run `./notey.py -e` and it will push your changes up to your remote repo
  * If for some reason allmark isn't doing the needful, you can restart it with `.\notey.py -a`

### TODO
  * Add templates for high level folders
  * add auto updating into allmark docker image so it sees changes on the fly
