# Django-Rest-Frame-Work-Web-Crawler
Project Title A web crawler utilizing a Django Rest Frame Work that can scrape articles of major blogs such as TechCrunch and stores them in a Posgresql database using docker-compose

Installation

Initialize PostgreSQL database locally:
-download from here: https://www.postgresql.org/download/
-create database, user_name, user_password
-grant readonlypriledges to user, as shown in here, by user IMSoP; https://stackoverflow.com/questions/6452956/how-to-create-a-user-with-readonly-privileges-for-all-databases-in-postgresql

Create a new directory for project
Create a new virtual environment with virtualenv: virtualenv 
Download ck_project files and folders to new directory
Set environment settings: set DJANGO_SETTINGS_MODULE=ck_project.settings.dev
Change Database in Settings.py and settings.base.py, update to your Name, User and Password
Enter virtualenvironment of project directory
Run: python manage.py makemigrations
python manage.py migrate
Runserver: python manage.py runserver
Open webcrawler in browser: localhost:8000

Prerequisites
Docker version 18.03.0-ce. Adjust: version: '3.6' in docker-compose.yaml according to your Docker Engine release version, see here: https://docs.docker.com/compose/compose-file/
Python 3.6
Pip, see here: https://pip.pypa.io/en/stable/installing/
PostgreSQL

Built with:
Python 3.6
Django Rest Frame Work
PostgreSQL

Deployment:
AWS Elastic Beanstalk
Create IAM user with the following permissions:
AWSElasticBeanstalkFullAccess - AWS Managed policy
AWSElasticBeanstalkService - AWS Managed policy
AWSCodeDeployRole - AWS Managed policy
AWSCodeDeployFullAccess - AWS Managed policy
Follow instructions https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html
