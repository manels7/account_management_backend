Please create a .env file based on .env-example where the required ENV variables will be defined.

### Postgres variables
POSTGRES_DB        : defines the database's name to be used. <br>
POSTGRES_USER      : defines the postgres username. <br>
POSTGRES_PASSWORD  : defines the postgres password. <br>

### Django variables
PORT : defines the port for the Django server (development mode)


Build docker from docker-compose
	cd docker/
	docker-compose build
	docker-compose up -d