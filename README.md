# flask-rest-pytest

The goal of this project is to demonstrate the creation of REST endpoints in Flask, the use of Pytest to validate endpoints without manual validation on the server, and the use of a virtual environment to isolate dependencies, designed to run on Ubuntu 24.04.2 LTS.


What does the Flask server do?

The Flask server maintains data in memory using a Python list, which acts as a temporary database. Through this list, four REST endpoints are implemented:

- GET: Its function is to return all stored elements.
- POST: Receives an item and adds it to the list.
- PUT: Updates/replaces an existing item in the list based on its location within the list.
- DELETE: Removes an existing item from the list based on its location within the list.

Note: The app.py file contains the Flask server implementation


What does the pytest script do?

The tests/test_app.py file automatically validates the functions of the Flask server endpoints.
This proves that the endpoints exist, respond correctly, and modify the data as expected.
It works by cleaning the data list before each test to avoid interference, and use app.test_client() to simulate HTTP requests.

The test check that:
- POST adds an item to the list
- GET returns a list containing all recurrent elements
- PUT correctly updates a specific element
- DELETE removes the correct element form the list


How to execute the project?

1. Open a new terminal in the project's root directory (top left corner with the three-line symbol).
2. Activate the included virtual environment, typing the following command in the terminal -> source virtual_environment/bin/activate
3. Activate the tests, typing the following command in the terminal -> PYTHONPATH=. pytest -v

After execution, Pytest will display the results of all endpoint validations.

Project Packaging (Wheel)

This project has been packaged into a wheel file, located in the dist/ folder.
A wheel is a pre-built Python package that contains all your code and allows for easy installation with pip.
To use the wheel file:
1. Verify that the wheel file is in the dist/ folder, typing the following command in the terminal -> ls dist/
2. Install it with pip, typing the following command in the terminal -> pip install dist/flask_rest_pytest-0.1-py3-none-any.whl
Once installed, the project can be imported from Python.

Note: This is optional. You can still run pytest without installing the wheel, as long as you have the virtual environment enabled.


------------------------------------ AI as a tool--------------------------------------------------------


During the development of this challenge, AI was used to support the resolution of specific problems, such as handling errors in the endpoints (for example: return jsonify({'error': 'Index out of range'}), 404), correcting issues with requests and connection errors when testing the endpoints, creating the setup.py file and packaging the project in Wheel.

In summary, AI helped solve the most difficult points and optimize the project, while the design, development, and testing of the server were implemented manually.