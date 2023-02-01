"""Test view machine route."""

import unittest

import requests
from flask import json

from services.vm_test_services import VendingTestServices

service: VendingTestServices = VendingTestServices()


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
        assert response.status_code == 200

    def test_view_machine_fail(self: "TestViewMachine") -> None:
        """Fail to view machine."""
        response: requests = requests.get(url=f"{service.get_machine_url}/0")
        assert response.status_code == 500

    def test_view_all_machines(self: "TestViewMachine") -> None:
        """Test view all machines route."""
        response: requests = requests.get(url=f"{service.all_machines_url}")
        assert response.status_code == 200

    def test_view_all_machines_fail(self: "TestViewMachine") -> None:
        """Fail to view all machines."""
        response: requests = requests.get(url=f"{service.all_machines_url}/0")
        assert response.status_code == 404


if __name__ == "__main__":
    unittest.main()
