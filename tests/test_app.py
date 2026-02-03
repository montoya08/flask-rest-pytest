import pytest  # Import the testing framework
from app.app import app, data # Import the Flask app and the list

class TestEndpoints: #The tests are grouped into a class to organize the code
    @pytest.fixture(autouse=True) # This function prepares the environment before running a test; "autouse=True" is what allows the function to run automatically
    def setup(self): # It is executed once per test
        self.client = app.test_client()  # Create a fake user to perform the test
        app.testing = True # It specifies that it is for testing
        data.clear() # Clear list before testing

    def test_post(self):
        response = self.client.post('/elements', json={'element': 'one'}) # Simulates a POST
        assert response.status_code == 200 # Verify that the endpoint responded correctly
        assert 'one' in response.json['data'] # Confirms that the item 'one' was saved

    def test_get(self):
        response = self.client.get('/elements') # Simulates a GET
        assert response.status_code == 200 
        assert isinstance(response.json, list) # Confirm that it returns a list

    def test_put(self):
        self.client.post('/elements', json={'element': 'two'})
        response =self.client.put('/elements/0', json={'element': 'three'}) # Simulates updating the element at index 0
        assert response.status_code == 200
        assert response.json['data'][0] == 'three' # Confirm that the value was replaced

    def test_delete(self):
        self.client.post('/elements', json={'element': 'four'}) # Create an item that will later be deleted
        response =self.client.delete('/elements/0') # Delete the first element
        assert response.status_code == 200
        assert'four' not in response.json['data'] # Confirm that the deleted item is no longer in the list