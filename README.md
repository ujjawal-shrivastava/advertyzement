# Advertyzement Assignment
This repo contains a Python/Django GraphQL API developed as an assignment.

[Heroku Deployment (GraphiQL).](https://advertyzement.herokuapp.com/gql/) 

## Overview
Task was to develop and deploy a GraphQL API using any Python framework.
Data was given in the form of an SQL Dump at [this repo](https://github.com/Amanskywalker/indian_banks).

## Libraries/Framworks

 - Django (ORM and Web Framework)
 - Graphene (GraphQL Implementation for Python)

## Approach

 - After examining the data provided, the framework of choice was Django
   because it comes with a robust ORM out of the box. It was simple to
   generate models from existing data using the inspectdb command.
   
 - I was initially perplexed by the GraphQL libraries Ariadne and
   Graphene. Both are fantastic; whereas Ariadne provides a lot more
   control, our modest project with Graphene will be a much simpler
   method.
   
 - While writing the code for the resolvers, I was confused between
   using the Branches (Table) model or the Bank Branches (View) model
   for the actual branches query because they both have many common
   values, except for the bank name and id. Bank might have been a
   sub-field within the branches query if I had used the Branches model.
   
 - I chose Bank Branches because it contained all of the fields. This
   allowed me to implement a Full text based search filter that searches
   across all of the data such as bank name, state, city, address, and
   even IFSC.
   
 - In both queries, I also included primitive pagination support with
   first and skip arguments.
   
 - Because the project was to be deployed to Heroku, the key issue was
   the database. The given data had about 127K rows, however Heroku Free
   Database only has 10K rows. So I took the original database and
   reduced it to about 9K rows. I built a database folder in the
   repository with two files: local.sql (Original, 127K rows) and
   production.sql (Changed, 9K rows).
   
 - I was able to successfully deploy the project. Two things I know I
   could have done better are, first to use git throughout the
   development time (I was in a rush and completed the project in one
   go) and second to set up Github Action Workflows, and have some test
   cases written (I still have to learn and improve on these things).

## Development
Clone the repo and change the current directory,

    git clone https://github.com/ujjawal-shrivastava/advertyzement.git
    cd advertyzement

Create the virtual environment and install dependecies,

    pipenv install

Create a new Postgres Database and then run the following command,

    psql -d database -U username -f ./databases/local.sql

Now create a new .env file and fill in the required variable values. (Refer .env.example file),

    DATABASE_URL=engine://username:password@host:port/databasename
    SECERET_KEY=ITS--A--SECRET
    DEBUG=False
    ALLOWED_HOSTS=['*']

Migrate the database with *--fake-inital* argument,

    python manage.py migrate --fake-initial

Create a superuser to access Django Admin Panel,

    python manage.py createsuperuser

Finally, run the development server,

    python manage.py runserver

If all the steps are completed successfully, the local server will serving the API [here](http://localhost:8000/gql/).

## 
