"""Test delete machine route."""

import unittest

import requests
from app import app
from flask import json
from services.vm_test_services import VendingTestServices

service: VendingTestServices = VendingTestServices()


class TestDeleteMachine(unittest.TestCase):
    """Test delete machine route."""

    def test_delete_machine(self: "TestDeleteMachine") -> None:
        """Test delete machine route."""
        all_machines_url: json = service.query_all_machines()
        if len(all_machines_url) == 0:
            machine_id: int = service.add_machine_if_empty("test", "test")
        else:
            machine_id: int = all_machines_url[0]["id"]
        response: requests = app.test_client().delete(url=f"{service.delete_machine_url}/{machine_id}")
        response_json: json = response.json()
        assert response.status_code == 200
        assert response_json["success"] is True

    def test_delete_machine_fail(self: "TestDeleteMachine") -> None:
        """Fail to delete machine."""
        response: requests = app.test_client().delete(url=f"{service.delete_machine_url}/-1")
        response_json: json = response.json()
        assert response.status_code == 404
        assert response_json["success"] is False


if __name__ == "__main__":
    unittest.main()
