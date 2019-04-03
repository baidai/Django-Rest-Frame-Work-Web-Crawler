FROM python:3.6

#Set pythonbuffered so output is displayed in the Docker log
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=ck_project.settings.base

# Set the working directory to /app
WORKDIR /ck_project

# Install any needed packages specified in requirements.txt
RUN pip install pipenv
COPY  Pipfile Pipfile.lock /ck_project/
RUN pipenv install --system

# Copy the current directory contents into the container at /ck_project
COPY . /ck_project

