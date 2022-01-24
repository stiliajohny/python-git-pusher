#!/bin/env python3

"""Make a script that takes a list f repositories and  pushes the same files to all of them"""

# import the python libraries required
import os
import sys
import argparse
import shutil
import logging
import re
import git
from pyfiglet import Figlet



# create banner
def banner():
    """Print the banner
    """
    try:
        # create a figlet object
        f = Figlet(font='slant')
        # print the banner
        print(f.renderText('Git-Pusher'))
    except Exception as e:
        logging.error(e)
        sys.exit()


# create a function that checks if a binary is installed on the system
def check_binary(binary):
    """ Check if a binary is installed on the system

    Args:
        binary (string): The binary to check

    Returns:
        bool: True if the binary is installed, False otherwise
    """
    logging.debug('Checking if \'' + binary + '\' is installed')
    try:
        # check if the binary is installed
        if shutil.which(binary):
            logging.debug('Binary \'' + binary + '\' is installed')
            return True
        else:
            logging.error('Binary \'' + binary + '\' is not installed')
            return False
    except Exception as e:
        logging.error(e)
        sys.exit()


# create a function for the argument parser
# add the arguments repo, file, action, verbosing
def arg_parser():
    """Create the argument parser

    Returns:
        object: An object containing the arguments
    """

    parser = argparse.ArgumentParser(description='Push files to multiple repos in one go', epilog='Use it with care :B')
    parser.add_argument('--repos', help='The repository to clone or the file contains a list of repository', required=True)
    parser.add_argument('--action', help='The action to perform', required=False)
    parser.add_argument('-v', '--verbose', help='Increase output verbosity', action='store_true')
    parser.add_argument('--temporary-location', help='The temporary location to clone the repository', default='/tmp', required=False)
    parser.add_argument('--branch', help='The branch to make', default='git-pusher', required=False)
    parser.add_argument('--commit-message', help='The commit message', default='Commited by the git-pusher', required=False)
    parser.add_argument('--file', help='The file(s) to push', required=True)
    args = parser.parse_args()
    return args


# create a functons that opens a file and return its context
def repo_list(repos):
    """ Create a list of repositories from a file or a string

    Args:
        repos (string): file containing a list of repositories or a single repository url
    Returns:
        dict: A dictionary containing the repositories
    """
    try:
        logging.debug('Creating a list of repositories')
        # check if path is string
        if isinstance(repos, str):
            # check if the file exists
            if os.path.isfile(repos):
                logging.debug('Using file: ' + repos)
                with open(repos, 'r') as f:
                    repos = f.readlines()
                logging.debug('Repositories: ' + str(repos))
                return repos
            # check if the string is a url ( git or fqdn )
            # https://regexr.com/59nrk
            elif re.match("^(([A-Za-z0-9]+@|http(|s)\:\/\/)|(http(|s)\:\/\/[A-Za-z0-9]+@))([A-Za-z0-9.]+(:\d+)?)(?::|\/)([\d\/\w.-]+?)(\.git){1}$", repos):
                logging.debug('Using regex pattern')
                logging.debug('Repository: ' + repos)
                return repos

            # if is not a file or a url exit
            else:
                logging.error('The file or url provided is not valid')
                sys.exit()
        else:
            logging.error('The input is not a string or not input provided')
            sys.exit()
    except Exception as e:
        if e == 'No such file or directory':
            logging.error('File does not exist: ' + repos)
        elif e == 'Not a valid URL':
            logging.error('Not a valid URL: ' + repos)
            sys.exit()
        else:
            logging.error(e)
            sys.exit()


# crete a funcition that clones a repository with a python module and return the path of the cloned repository
def clone_repo(repo, temp_location):
    """Clone a repository
    Args:
        repo (string): The repository to clone ( file or url )
        temp_location (string): The temporary location to clone the repository
    """
    # remove any new lines from the repo name
    repo = str(repo.strip('\n'))
    repo_folder = repo.split('/')[-1].split('.')[0]
    temp_repo_folder = temp_location + '/' + repo_folder
    try:
        logging.info('Pre-clonning checks')
        # return the last part of the string before .git
        # check if the folder exists
        if os.path.isdir(temp_repo_folder):
            logging.info('Folder already exists: ' + temp_repo_folder)
        if os.path.isdir(temp_repo_folder):
            logging.info('Removing old repo: ' + repo_folder)
            shutil.rmtree(temp_location + '/' + repo_folder)
        logging.info('Cloning repository: ' + repo)
        # use the git module to clone the repository
        repo = git.Repo.clone_from(repo, temp_repo_folder)
    except Exception as e:
        logging.error(e)
        sys.exit()


# create a function that copies a file to a repository
def copy_file(repo, temp_location, file):
    """Copy a file to a locaton in a repository

    Args:
        repo (string): The repository to clone ( file or url )
        temp_location (string): The temporary location to clone the repository
        file (string): The file to copy
    """
    # remove any new lines from the repo name
    repo = repo.strip('\n')
    localfile = file.split('/')[-1]
    temp_location_file = temp_location + '/' + repo.split('/')[-1].split('.')[0] + '/' + localfile
    logging.info('Copying file: ' + file + ' to ' + temp_location_file)
    try:
        # check if the file exists on the temp directory
        if os.path.isfile(temp_location_file):
            logging.error('File already exists: ' + temp_location_file)
            sys.exit()
        else:
            # use file instead of localfile as we need the relative path of the original file to copy
            logging.info('Copying file: ' + file + ' to ' + temp_location_file)
            # use shutil to copy the file itself to the temp location of the repo
            shutil.copy(file, temp_location_file)
    except Exception as e:
        logging.error(e)
        sys.exit()

# create a function that makes a new branch on the cloned repository
def make_branch(repo, temp_location, branch):
    # remove any new lines from the repo name
    repo = repo.strip('\n')
    temp_repo_folder = temp_location + '/' + repo.split('/')[-1].split('.')[0]
    try:
        logging.debug('Making branch: ' + branch)
        # use the git module to make a new branch
        repo = git.Repo(temp_repo_folder)
        repo.git.checkout(b=branch)


    except Exception as e:
        logging.error(e)
        sys.exit()


# commit a file on the cloned repository
def commit_file(repo, temp_location, file, commit_message):
    """Commit a file to a repository

    Args:
        repo (str | list): The repository to clone ( file or url )
        temp_location (str): The temporary location to clone the repository
        file (str): The file to commit
        commit_message (str): The commit message
    """
    # remove any new lines from the repo name
    repo = repo.strip('\n')
    localfile = file.split('/')[-1]
    temp_repo_folder = temp_location + '/' + repo.split('/')[-1].split('.')[0]
    try:
        logging.debug('Commiting file: ' + file)
        # use the git module to commit the file
        repo = git.Repo(temp_repo_folder)
        repo.git.add(localfile) # use the filename only instead of th erelative path
        repo.git.commit(m=commit_message)

    except Exception as e:
        logging.error(e)
        sys.exit()


# pull the latest changes from the cloned repository
def pull_repo(repo, temp_location):
    """Pull the latest changes from the cloned repository

    Args:
        repo (str | list): The repository to clone ( file or url )
        temp_location (str): The temporary location to clone the repository
    """
    # remove any new lines from the repo name
    repo = repo.strip('\n')
    temp_repo_folder = temp_location + '/' + repo.split('/')[-1].split('.')[0]
    try:
        logging.info('Pulling latest changes')
        # use the git module to pull the latest changes
        repo = git.Repo(temp_repo_folder)
        # pull all the branches
        repo.git.pull()

    except Exception as e:
        logging.error(e)
        sys.exit()


# check if the branch exists on the cloned repository
def check_branch(repo, temp_location, branch):
    """Check if the branch exists on the cloned repository

    Args:
        repo (str | list): The repository to clone ( file or url )
        temp_location (str): The temporary location to clone the repository
        branch (str): The branch to check
    """
    # remove any new lines from the repo name
    repo = repo.strip('\n')
    temp_repo_folder = temp_location + '/' + repo.split('/')[-1].split('.')[0]
    try:
        logging.debug('Checking branch: ' + branch)
        # use the git module to check if the branch exists
        repo = git.Repo(temp_repo_folder)
        remote = repo.remote()
        logging.debug('Remote: ' + str(remote))
        # return the names of all the branches
        for ref in repo.references:
            # print the name of the branch wihout the remote
            logging.debug(ref.name.split('/')[-1])
            # check if the branch exists
            if ref.name.split('/')[-1] == branch:
                logging.error('Branch exists: ' + branch)
                sys.exit()

    except Exception as e:
        logging.error(e)
        sys.exit()

# push the changes to the remote repository
def push_changes(repo, temp_location, branch):
    """Push the changes to the remote repository

    Args:
        repo (string): The repository to clone ( file or url )
        temp_location (string): The temporary location the repository is cloned
        branch (string): The branch to push
    """
    # remove any new lines from the repo name
    repo = repo.strip('\n')
    temp_repo_folder = temp_location + '/' + repo.split('/')[-1].split('.')[0]
    try:
        logging.debug('Pushing changes to remote repository')
        logging.info('Pushing changes to branch: ' + branch)
        # use the git module to push the changes to the remote repository
        repo = git.Repo(temp_repo_folder)
        # push the current branch and set the remote as upstream,
        repo.git.push('--set-upstream', 'origin', branch)

    except Exception as e:
        logging.error(e)
        sys.exit()


# check the if argument verboose is set and return DEBUG or INFO
def check_verbose(args):
    """Check if the verbose argument is set and return DEBUG or INFO"""
    if args.verbose:
        return logging.DEBUG
    else:
        return logging.INFO


def main():
    """Main function"""
    banner()
    args = arg_parser()
    log_format = '%(asctime)s - %(levelname)5s - %(filename)15s:%(lineno)5s - %(funcName)15s()  - %(message)s'
    logging.basicConfig(level=check_verbose(args), format=log_format)
    check_binary('git')

    repos = repo_list(args.repos)
    for line in repos:
        clone_repo(line, args.temporary_location)
        # pull_repo(args.repos, args.temporary_location)
        check_branch(line, args.temporary_location, args.branch)
        make_branch(line, args.temporary_location, args.branch)
        copy_file(line, args.temporary_location, args.file)
        commit_file(line, args.temporary_location, args.file, args.commit_message)
        push_changes(line, args.temporary_location, args.branch)


if __name__ == '__main__':
    main()
