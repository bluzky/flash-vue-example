# Lemon project

This provide simple function: analyze given url for langue usage statistics.

- Client with simple form for user input
- Responsive layout
- Load from database if url has been analyzed already.
- Allow user to ignore cache and run a fresh analyzing
- Display top 100 word with bar chart
- Easy to start project with docker compose

## How to start

- Required docker installed on your machine
- Jump to project dir and run
  ```
  docker-compose up
  ```
- Access web client at [http://localhost:5100/](http://localhost:5100/)
- Access server at [http://localhost:5001/](http://localhost:5001/)

## Server

### Tech & library
Server use Flask framework and list of following tech and libraries

- `sqlite` for database
- `Flask-Migrate/alembic` for database migration
- `SQLAlchemy` via Flask-SQLAlchemy for ORM
- `WTForm` for param validation
- `beautifulsoup4` to extract text from html document
- `pipenv` to manage dependencies


### Main modules

- `app.py` main entrypoint
- `database.py` define database instance and base model class
- `models.py` define models for SQLAlchemy
- `services.py` define business logic for reusability
- `forms.py` define forms for params validation
- `web_scrapper.py` define Class that analyze URL

## Client

### Tech & library
Client use Vue framework with following libraries:

- `axios` to make request. Can use fetch for simple, here I use `axios` to test `provide/inject` feature of Vue.
- `chartjs` via `vue-chartjs` to render chart
- `tailwindcss` for quick styling

### Main components
- `HomeView`: Main component for this app
- `LoadingMessage`: stateless component for showing message while submitting request to server
- `AnalyzingSummary`: Show some details of execution and webpage content
- `TopWords`: display a bar chart of most used words, order by descending order
