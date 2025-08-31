# API Automation Framework (Pytest + Requests)
This is an **API automation framework** built using **Python, Pytest, and Requests**.  
I have used [DummyJSON APIs](https://dummyjson.com/) with configuration- driven setup, fixtures and test file.

## Structure

```project/
│── configuration/
│ └── config.ini # Stores URL, credentials
│
│── utilities/
│ └── read_properties.py # Reads values from config.ini
│
│── conftest.py # Pytest fixtures (login, base_url, etc.)
│
│── tests/
│ ├── test_login.py # Tests login API (/auth/login)
│ ├── test_products.py # Tests product endpoints (/products)
│ └── test_current_user.py # Tests current user endpoint (/auth/me)
│
│── pytest.ini # Pytest config (markers, options)
│── requirements.txt # Python dependencies
│── README.md # Project documentation
```
---

## Install dependencies

```pip install -r requirements.txt```


## Git Repo

```https://github.com/varuu09/Frejun```

## Fixtures
Defined in conftest.py:

login  Logs in once per session, returns a dictionary with:
-status_code
-headers
-token

## Run Test
```pytest``` -Run all tests
```pytest src/test_products.py``` -Run a specific test file
```pytest src/current_user/test_current_user.py::Test_current_user::test_current_user``` -Run specific function

## Reports
```pytest --html=report.html --self-contained-html --metadata Url https://dummyjson.com/ ```


## Covered Scenarios

Login API /auth/login
-Valid login → returns token
-Invalid credentials → returns error

Products API /products
-Get all products
-Search products
-Invalid product ID

Current User API /auth/me
-with valid token → returns user details
-without token → returns 401 Unauthorized

