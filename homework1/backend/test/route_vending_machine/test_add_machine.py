import os
import requests
import unittest
from services import test_services
from dotenv import load_dotenv

load_dotenv()

local_host_address = os.environ["LOCALHOST_ADDR"]

add_machine_url = f"{local_host_address}/add_machine"


class TestAddMachine(unittest.TestCase):
    def test_add_machine(self):
        test_location = test_services.random_string_for_test()
        test_name = test_services.random_string_for_test()
        response = requests.post(
            url=add_machine_url, data={"name": test_name, "location": test_location}
        )
        response_json = response.json()
        assert response.status_code == 201
        assert response_json["name"] == test_name
        assert response_json["location"] == test_location
        return response_json["id"]

    def test_add_machine_fail(self):
        response = requests.post(url=add_machine_url)
        assert response.status_code == 400


if __name__ == "__main__":
    unittest.main()
