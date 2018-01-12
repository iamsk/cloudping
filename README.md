

# cloudping

This project has the following basic apps:

* ping - the core app which implement the main logic.

## Installation

To set up a development environment quickly, install Python 2.x first. It
comes with virtualenv built-in. so create a virtual environment with:

`mkvirtualenv cloudping`

Install dependencies:

`pip install -r requirements.txt`

Run server:

`python manage.py runserver --settings=cloudping.settings.development`
