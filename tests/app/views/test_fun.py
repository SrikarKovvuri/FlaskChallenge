def test_vacation(client):
    response = client.get("/fun/vacation")

    assert(response.status_code == 200)
    assert(response.json == {'vacation': True})

def test_holiday(client):
    response = client.get("/fun/holiday")

    assert(response.status_code == 401)