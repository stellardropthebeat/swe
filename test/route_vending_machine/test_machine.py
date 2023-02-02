import secrets
import string

from app import app
from bs4 import BeautifulSoup
from flask import json

parser = "html.parser"

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
    machines = app.test_client().get(all_machines_url).data
    soup = BeautifulSoup(machines, parser)
    line = soup.find("li").find("a").get("href")
    lid = line[line.rfind("/") + 1 :]
    return lid


def random_json() -> dict:
    """Get a random json."""
    rand_json = {"name": random_string(5), "location": random_string(5)}
    return rand_json


def test_add_machine() -> None:
    """Test add machine route."""
    test_json: json = random_json()
    name: str = test_json["name"]
    location: str = test_json["location"]
    app.test_client().post(add_url, data=test_json)

    machines = app.test_client().get(all_machines_url).data
    soup = BeautifulSoup(machines, parser)
    assert name == soup.find(text=name)
    assert location == soup.find(text=location)


def test_update_machine() -> None:
    """Test update machine route."""
    test_json: json = random_json()
    machine_id: str = get_id()
    new_name: str = test_json["name"]
    new_location: str = test_json["location"]
    app.test_client().post(f"{update_url}/{machine_id}", data=test_json)

    machines = app.test_client().get(all_machines_url).data
    soup = BeautifulSoup(machines, parser)
    assert new_name == soup.find(text=new_name)
    assert new_location == soup.find(text=new_location)


def test_delete_machine() -> None:
    """Test delete machine route."""
    machine_id: int = get_id()
    app.test_client().delete(f"{delete_url}/{machine_id}")

    machines = app.test_client().get(all_machines_url).data
    soup = BeautifulSoup(machines, parser)
    assert soup.find("a", {"id": machine_id}) is None
