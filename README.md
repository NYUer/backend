# backend

Welcome to the backend repo of Swift Planner!

## Description

Our backend processes information obtained from NYU RESTful API and then sends it to frontend via RESTful API.

See our API documentation here:

**[API Documentation](https://github.com/NYUer/backend/tree/master/nyuapi)**

##  Directory Structure
* [./venv3](https://github.com/NYUer/backend/tree/master/venv3) is the virtual environment for our project. Run our project under this virtual environment to prevent dependency issue.
* [./nyuapi](https://github.com/NYUer/backend/tree/master/nyuapi) is a python module which incapsulates NYU RESTful API into a python class.
* [app.py](https://github.com/NYUer/backend/blob/master/app.py) is a simple Flask http request handler.
