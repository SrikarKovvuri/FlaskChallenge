def test_au(client):
    response = client.get("/goodbye/au_revoir")
    
    assert(response.status_code == 200)
    assert(response.json == {'au_revoir': True})

def test_see(client):
    response = client.get("/goodbye/see_ya")
    
    assert(response.status_code == 200)
    assert(response.json == {'see_ya': True})
