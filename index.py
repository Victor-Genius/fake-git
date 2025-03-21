import requests
import json
import os
from subprocess import call, Popen, PIPE

def fake_repository(url, username):
    print("Faking " + url)
    git_url = 'https://github.com/' + username + '/' + url + '.git'
 
    os.system('git clone ' + git_url) # clone


    os.chdir(url)
    os.system('git branch -M main')
    os.system("""
                git filter-branch -f --env-filter \
                    "GIT_AUTHOR_NAME='{}'\
                     GIT_AUTHOR_EMAIL='{}'\
                     GIT_COMMITTER_NAME='{}'\
                     GIT_COMMITTER_EMAIL='{}'\
                     " HEAD\
                """.format(g_name, g_email, g_name, g_email))
    os.chdir('../')

    print("Success fake " + url)

def push_repository(url):
    print("Pushing " + url)
    os.chdir(url)
    os.system('gh repo create {} --public'.format(url))
    os.system('git remote remove origin')
    os.system('git remote add origin https://github.com/{}/{}'.format(g_name, url))
    os.system('git config user.name {}'.format(g_name))
    os.system('git config user.email {}'.format(g_email))
    os.system('git push -u origin main')
    os.chdir('../')

    print("Success push " + url)

if __name__ == '__main__':
    #response = requests.get('https://api.github.com/users/gitusername/repos')
    #repositories = json.loads(response.text)

    # g_name = input('Enter your github user name: ')
    # g_email = input('Enter your github user email: ')

    # g_name = 'supervenus0204'
    # g_email = 'supervenus0204@gmail.com'

    g_name = 'robertjacks'
    g_email = 'robertjacks0204@gmail.com'


    f = open("need_unfork.txt", "r", encoding='utf8')
    repositories = f.readlines()

    print(repositories)
    for repo in repositories:
        url_list = repo.split("/")
        print(url_list)
        url = url_list[4].replace("\n", "")
        username = url_list[3].replace("\n", "")
        print(url)
        fake_repository(url, username)
        push_repository(url)

    f.close()
