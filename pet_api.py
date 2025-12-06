import requests

BASE_URL = "https://petstore.swagger.io/v2"


def add_pet (pet_body: dict):
    url = BASE_URL + "/pet"
    return requests.post(url, json=pet_body)


def get_pet_by_id (pet_id: int):
    url = BASE_URL + f"/pet/{pet_id}"
    return requests.get(url)

def delete_pet (pet_id: int):
    url = BASE_URL + f"/pet/{pet_id}"
    return requests.delete(url)


def update_pet(pet_body: dict):
    url = BASE_URL + "/pet"
    return requests.put(url, json=pet_body)

def make_pet_body (pet_id: int, name: str = "TestPet", status:str = "available"):
    return {
        "id": pet_id,
        "name": name,
        "status": status
    }

