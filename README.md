mypython
========

Python 3.7 Docker Env with local PostgreSQL

# Pre Reqs
* Docker installed
* dockerhub access

#  Setup Python 3.7 Docker Env
Clone this repository first and build your python image.  This Dockerfile is using python:3.7-stretch with additional python libraries, pip, and pipenv.  This image also includes a PostgreSQL client and the awscli.

```
docker build -t <dockerhub_account>/mypython3.7 .
```

Use a bash function to simplify starting your docker container.  Review setEnv.sh and customize to meet your needs.
```
source setEnv.sh
mypython bash
cd /root/Projects/python/myproject
pipenv --python python3.7 install flask python-dotenv psycopg2-binary Flask-SQLAlchemy
pipenv shell
```

# Setup the sample PostgreSQL DB
You can use any PostgreSQL DB you have a route to or run on locally by following these steps.

Make sure you have docker installed and access to the internet.  The db_setup.sh script will ask you to set db $POSTGRES_USER / $POSTGRES_PASSWORD, and defaults the $POSTGRES_DB='sample'.  It will import 1000 rows of sample data and setup the container to list on ports 80 and 5432
```
cd docker/scripts
./db_setup.sh
```
The db_setup.sh script can install docker on CentOS if required.  I have commented this secton out assuming this prereq is already in place for your environment.

Test your connectivity with PostgreSQL client (psql)
```
psql postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@localhost:80/sample -c "SELECT count(id) FROM employees;"

count
-------
  1000
(1 row)
```

Note: You can do this same test using a container if you dont have the client locally installed.
```
docker run -it --rm postgres psql postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${MY_IP}:80/sample -c "SELECT count(id) FROM employees;"
```

## Setup or add a local PostgreSQL DB from a dump.
This is assuming you have a local postgres container as your DB and you want to import/update it.
1. For a new DB only.  Connect to the running container and create the db.
```
docker exec -i postgres psql postgres -U $POSTGRES_USER -c "CREATE DATABASE <DB_NAME>;”
```
2. create/restore the db
```
psql postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${MY_IP}/<DB_NAME> < <DB_NAME>_roles.sql
psql postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${MY_IP}:80/<DB_NAME> < <DB_NAME>.sql.dump
```

## Exporting a dump from the remote DB if not available.

1. use pg_dumpall to get roles.
```
pg_dumpall -h $REMOTE_HOST -p 5432 -U ${POSTGRES_USER} -v --roles-only -f "./<DB_NAME>_roles.sql”
```
2. Use pg_dump to export the db.
```
pgdump -h $REMOTE_HOST -p 5432 -U ${POSTGRES_USER} dbname > ./<DB_NAME>_dump.sql
```
