#!/usr/bin/env python
import os
import shutil
from git import Repo
import datetime

MAIN_ROOT = '/home/rafrom3/anaruiz.club'
PROJECT = 'anaruiz'

PROJECT_ROOT = os.path.join(MAIN_ROOT, PROJECT)
PUBLIC_ROOT = os.path.join(MAIN_ROOT, 'public')
STATIC_ROOT = os.path.join(PUBLIC_ROOT, 'static')
TMP_ROOT = os.path.join(MAIN_ROOT, 'tmp')
BACKUPS_ROOT = os.path.join(MAIN_ROOT, 'backups')
DB_ROOT = PROJECT_ROOT

db_backup_done = False


# DataBase Backup
if not os.path.exists(BACKUPS_ROOT):
    os.makedirs(BACKUPS_ROOT)

if os.path.exists(DB_ROOT):
    current_date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    bu_file_name = current_date + '_db.sqlite3'
    
    copy_db = 'cp ' + DB_ROOT + '/db.sqlite3 ' + BACKUPS_ROOT + '/' + bu_file_name
    os.system(copy_db)
    db_backup_done = True
    print(copy_db)
    print('Database Backup Done')
    print()


# If the Backup has been correctly done
if db_backup_done:

    if os.path.exists(PROJECT_ROOT):
        shutil.rmtree(PROJECT_ROOT)
        print(PROJECT_ROOT, 'folder deleted')
    
    if os.path.exists(STATIC_ROOT):
        shutil.rmtree(STATIC_ROOT)
        print(STATIC_ROOT, 'deleted')
    
    GIT_URL = 'https://github.com/Quitiweb/' + PROJECT
    DEST_NAME = PROJECT_ROOT

    cloned_repo = Repo.clone_from(GIT_URL, DEST_NAME)
    print(GIT_URL)
    print(DEST_NAME, 'cloned succesfully')
    print()


    # Recover the Database
    recover_db = 'cp ' + BACKUPS_ROOT + '/' + bu_file_name + ' ' + DB_ROOT + '/db.sqlite3'
    os.system(recover_db)
    print(recover_db)
    print('Database recovered')
    print()


    # settings/prod.py replacements
    manage_file = PROJECT_ROOT + '/manage.py'
    wsgi_file = os.path.join(PROJECT_ROOT, PROJECT) + '/wsgi.py'
    prod_settings = "sed -i 's/settings.dev/settings.prod/g' " + manage_file
    print(prod_settings)
    
    os.system(prod_settings)
    
    prod_settings = "sed -i 's/settings.dev/settings.prod/g' " + wsgi_file
    print(prod_settings)
    
    os.system(prod_settings)    


    # MakeMigrations
    make_migrations = 'python ' + manage_file + ' makemigrations'
    print(make_migrations)
    
    os.system(make_migrations)
    

    # Migrate
    migrate = 'python ' + manage_file + ' migrate'
    print(migrate)
    
    os.system(migrate)


    # CollectStatic
    collect = 'python ' + manage_file + ' collectstatic'
    print(collect)
    
    os.system(collect)
    
    touch = 'touch ' + TMP_ROOT + '/restart.txt'
    print(touch)
    
    os.system(touch)
