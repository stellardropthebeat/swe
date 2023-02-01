"""Test view machine route."""

import unittest

import requests
from flask import json
from services.test_vm_services import TestVendingServices

service: TestVendingServices = TestVendingServices()


class TestViewMachine(unittest.TestCase):
    """Test view machine route."""

    def test_view_machine(self: "TestViewMachine") -> None:
        """Test view machine route."""
        all_machines_url: json = service.query_all_machines()
        if len(all_machines_url) == 0:
            machine_id: int = service.add_machine_if_empty("test", "test")
        else:
            machine_id: int = all_machines_url[0]["id"]
        response: requests = requests.get(url=f"{service.get_machine_url}/{machine_id}")
        response_json: json = response.json()
        assert response.status_code == 200
        assert response_json["success"] is True

    def test_view_machine_fail(self: "TestViewMachine") -> None:
        """Fail to view machine."""
        response: requests = requests.get(url=f"{service.get_machine_url}/-1")
        response_json: json = response.json()
        assert response.status_code == 404
        assert response_json["success"] is False

    def test_view_all_machines(self: "TestViewMachine") -> None:
        """Test view all machines route."""
        response: requests = requests.get(url=service.all_machines_url)
        response_json: json = response.json()
        assert response.status_code == 200
        assert response_json["success"] is True

    def test_view_all_machines_fail(self: "TestViewMachine") -> None:
        """Fail to view all machines."""
        response: requests = requests.get(url=f"{service.all_machines_url}/-1")
        response_json: json = response.json()
        assert response.status_code == 404
        assert response_json["success"] is False


if __name__ == "__main__":
    unittest.main()
