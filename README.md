# Notey

## Summary 

Notey was developed to be way for me to manage my notes using markdown, sublime, and git.

## Prerequisites
  * Be on a mac or Linux -- no Windows support currently
  * Docker installed 
  * Git installed and configured
  * Your favorite text editor; I use Sublime but Atom is also super great
    * I recommend setting sublime to save on loss of focus with this line in your sublime settings page `"save_on_focus_lost": true`

## Usage

### Initial Setup
  * Create a private git repo
  * Clone the repo to the folder you want your notes stored in via 
    * git clone git@ggitrepo.com:repo_path.git"
  * Change the `working_dir` variable in notey.py to the folder where the .git file is located
  * It's a good idea to customize the list of top level folders to your needs
  * make python scripts executable via
    * `chmod +x notey.py`
  * run initial_run.py via `./notey.py -f`
  * This will create all necessary directories and file paths
  * Open directory in Sublime and edit files to your hearts content

### Daily Usage
  * Run `notey.py -s` to create a new daily notes file in the correct directory
  * This notes file will be populated with a template you can modify
  * Open a web browser and navigate to http://localhost:8888 to view your notes in markdown
  * When you want to save your work, run `./notey.py -e` and it will push your changes up to your remote repo
  * If for some reason allmark isn't doing the needful, you can restart it with `.\notey.py -a`

### TODO
  * Add scripts for new high level folder create
  * Add templates for high level folders