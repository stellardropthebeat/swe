import os
import random
import requests
import unittest
from dotenv import load_dotenv
from services import test_services

load_dotenv()

local_host_address = os.environ["LOCALHOST_ADDR"]
view_all_machine_url = f"{local_host_address}/all_machines"
machines_response = (requests.get(url=view_all_machine_url)).json()


class TestUpdateMachine(unittest.TestCase):
    def test_update_machine_success(self):
        if len(machines_response) == 0:
            create_machine_url = f"{local_host_address}/add_machine"
            test_location = test_services.random_string_for_test()
            test_name = test_services.random_string_for_test()
            response_json = (
                requests.post(url=create_machine_url, data={"name": test_name, "location": test_location})
            ).json()
            machine_id = response_json["id"]
        else:
            machine_id = random.choice(machines_response)["id"]
        new_test_location = test_services.random_string_for_test()
        new_test_name = test_services.random_string_for_test()
        update_machine_url = f"{local_host_address}/update_machine/{machine_id}"
        response = requests.post(
            url=update_machine_url, data={"name": new_test_name, "location": new_test_location}
        )
        response_json = response.json()
        assert response.status_code == 200
        assert response_json["location"] == new_test_location

    def test_update_machine_fail_no_params(self):
        if len(machines_response) == 0:
            create_machine_url = f"{local_host_address}/machine/create"
            test_location = test_services.random_string_for_test()
            test_name = test_services.random_string_for_test()
            response_json = (
                requests.post(url=create_machine_url, data={"name": test_name, "location": test_location})
            ).json()
            machine_id = response_json["id"]
        else:
            machine_id = random.choice(machines_response)["id"]
        update_machine_url = f"{local_host_address}/update_machine/{machine_id}"
        response = requests.post(url=update_machine_url)
        assert response.status_code == 400

    def test_update_machine_fail_no_machine(self):
        machine_ids = [machine["id"] for machine in machines_response]
        random_id = random.randint(0, max(machine_ids) * 10)
        while random_id in machine_ids:
            random_id = random.randint(0, max(machine_ids) * 10)
        new_mock_location = test_services.random_string_for_test()
        new_test_name = test_services.random_string_for_test()
        edit_machine_url = f"{local_host_address}/update_machine/{random_id}"
        response = requests.post(
            url=edit_machine_url, data={"name": new_test_name, "location": new_mock_location}
        )
        assert response.status_code == 404


if __name__ == "__main__":
    unittest.main()
