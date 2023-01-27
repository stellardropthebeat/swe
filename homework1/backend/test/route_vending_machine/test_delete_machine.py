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


class TestDeleteMachine(unittest.TestCase):
    def test_delete_machine_success(self):
        if len(machines_response) == 0:
            add_machine_url = f"{local_host_address}/add_machine"
            test_location = test_services.random_string_for_test()
            test_name = test_services.random_string_for_test()
            response_json = (
                requests.post(url=add_machine_url, data={"name": test_name, "location": test_location})
            ).json()
            machine_id = response_json["id"]
        else:
            machine_id = random.choice(machines_response)["id"]
        delete_machine_url = f"{local_host_address}/delete_machine/{machine_id}"
        response = requests.delete(url=delete_machine_url)
        assert response.status_code == 204

    def test_delete_machine_fail_no_machine(self):
        machine_ids = [machine["id"] for machine in machines_response]
        random_id = random.randint(0, max(machine_ids) * 10)
        while random_id in machine_ids:
            random_id = random.randint(0, max(machine_ids) * 10)
        delete_machine_url = f"{local_host_address}/delete_machine/{random_id}"
        response = requests.delete(url=delete_machine_url)
        assert response.status_code == 404


if __name__ == "__main__":
    unittest.main()
