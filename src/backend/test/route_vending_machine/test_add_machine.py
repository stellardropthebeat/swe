"""Test add machine route."""

import unittest

import requests
from flask import json
from services.vm_test_services import VendingTestServices

service: VendingTestServices = VendingTestServices()


class TestAddMachine(unittest.TestCase):
    """Test add machine route."""

    def test_add_machine(self: "TestAddMachine") -> None:
        """Test add machine route."""
        response = service.add_machine("test", "test")
        assert response.status_code == 201

        # Check response data
        response_json: json = response.json()
        assert response_json["success"] is True

    def test_add_machine_fail(self: "TestAddMachine") -> None:
        """Fail to add machine."""
        fail_test_json = {"name": "test"}
        response: requests = requests.post(url=service.add_machine_url, json=fail_test_json)
        assert response.status_code == 500


if __name__ == "__main__":
    unittest.main()
