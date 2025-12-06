from pet_api import add_pet, get_pet_by_id, delete_pet, make_pet_body, update_pet


def test_create_and_get_pet():
    
    pet = make_pet_body(123123123, name = "CreatedPet")
    

    create_resp = add_pet (pet)
    assert create_resp.status_code == 200


    get_resp = get_pet_by_id(pet["id"])
    assert get_resp.status_code == 200

    data = get_resp.json()
    assert data["id"] == pet["id"]
    assert data["name"] == pet["name"]
    assert data["status"] == pet["status"]

def test_update_pet():
    pet = make_pet_body(321321321, name="OldName")
    
    add_resp = add_pet(pet)
    assert add_resp.status_code == 200
    
    new_name = "NewName"
    pet["name"] = new_name
    new_status = "sold"
    pet["status"] = new_status
    
    update_resp = update_pet(pet)
    assert update_resp.status_code == 200
    
    get_resp = get_pet_by_id(pet["id"])
    assert get_resp.status_code == 200
    data = get_resp.json()
    assert data["name"] == new_name
    assert data["status"] == new_status
    
def test_pet_with_same_id():
    pet1 = make_pet_body(400400400, name = "FirstVersion", status="available")
    pet2 = make_pet_body(400400400, name = "SecondVersion", status="sold")
    
    resp1 =add_pet(pet1)
    assert resp1.status_code == 200
    
    resp2 = add_pet(pet2)
    assert resp2.status_code == 200
    
    get_resp = get_pet_by_id(400400400)
    assert get_resp.status_code == 200
    
    data = get_resp.json()
    assert data["name"] == "SecondVersion"
    assert data["status"] == "sold"

def test_delete_pet():
    pet = make_pet_body(88888,name = "ToBeDeleted")

    add_resp = add_pet(pet)
    assert add_resp.status_code == 200
    
    delete_resp = delete_pet(pet["id"])
    assert delete_resp.status_code in (200, 204, 404)
        
    get_resp = get_pet_by_id(pet["id"])
    assert get_resp.status_code == 404
    
    
def test_nonexistent_pet_returns_404():
    get_resp = get_pet_by_id(999912399)
    assert get_resp.status_code == 404
    