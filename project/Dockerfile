# pull official base image
FROM python:3.8-slim-buster

# set working directory
WORKDIR /usr/src/app

# install python dependencies
RUN python -m pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .

# conditonally create the tmp directory if it dosen't exist
RUN if [[ ! -d ./tmp ]]; then mkdir ./tmp
# check if the google cred exist in an env var and stream the content of the var to a file in ./tmp
RUN if [[ -z $GOOGLE_CREDS ]]; then echo "DBG: PLEASE UPDATE THE GOOGLE_CREDS ENV VAR"; else echo $GOOGLE_CREDS > ./tmp/google.json
