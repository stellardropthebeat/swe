import secrets
import string

from flask import json

from src.app import app

add_url: str = "/add_machine"
delete_url: str = "/delete_machine"
update_url: str = "/update_machine"
all_machines_url: str = "/all_machines"


def random_string(length: int) -> str:
    """Get a random string."""
    rand_str = "".join(secrets.choice(string.ascii_letters) for _ in range(length))
    return rand_str


def get_id() -> int:
    """Get the first machine_id found."""
    machines = app.test_client().get(all_machines_url).get_json()
    machine_id = machines[0]["id"]
    return machine_id


def random_json() -> json:
    """Get a random json."""
    rand_json = {"name": random_string(5), "location": random_string(5)}
    return json.dumps(rand_json)


def test_add_machine() -> None:
    """Test add machine route."""
    test_json: json = random_json()
    success: bool = True
    result: json = app.test_client().post(add_url, data=test_json, content_type="application/json").get_json()
    assert success == result["success"]


def test_update_machine() -> None:
    """Test update machine route."""
    test_json: json = random_json()
    machine_id: int = get_id()
    success: bool = True
    result: json = (
        app.test_client().put(f"{update_url}/{machine_id}", data=test_json, content_type="application/json").get_json()
    )
    assert success == result["success"]


def test_delete_machine() -> None:
    """Test delete machine route."""
    machine_id: int = get_id()
    success: bool = True
    result: json = app.test_client().delete(f"{delete_url}/{machine_id}").get_json()
    assert success == result["success"]


def test_render_index_page() -> None:
    """Test render page."""
    response: int = app.test_client().get("/").status_code
    assert response == 200


def test_render_machine_page() -> None:
    """Test render page."""
    response: int = app.test_client().get("/machines").status_code
    assert response == 200
