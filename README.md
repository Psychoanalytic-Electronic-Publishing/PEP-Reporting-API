


# PEP Reporting API

This Flask API facilitates error reporting for PEP.

---
## Getting Started

For local development you can run this as a regular Flask app.

### Prerequisites

For local development:
- [Python](https://www.python.org/)
- [Pip](https://pip.pypa.io/en/stable/) (comes with Python)

### Virtual Environment

As a best practice, set up a Python virtual environment. ([More info](https://virtualenv.pypa.io/en/latest/))


Install library:
```
pip install virtualenv
```

Create your virtual environment:
```
virtualenv venv
```

Begin using your virtual environment:
```
source venv/bin/activate
```

To stop using when you are done:
```
deactivate
```

### Running

#### Install Requirements
```
make install
```

#### Run Tests
```
make test
```

#### Run the app

To set up properties, update `flask-config-overwrite.json` then run:

```
make run
```
## API Documentation

Once you are running the app the main page points to a Swagger documentation of the API.
