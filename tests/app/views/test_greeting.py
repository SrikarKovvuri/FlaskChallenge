
def test_dummy(srikars_fixture):
    assert(srikars_fixture == "Hello")

def test_salut(client):
    response = client.get("/greetings/salut")
    
    assert(response.status_code == 200)
    assert(response.json == {'salut': True})

def test_hello(client):
    response = client.get("/greetings/hello")

    assert(response.status_code == 404)


  