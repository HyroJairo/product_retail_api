def test_register_get(client):
    data = {
        "name": "Mustafa",
        "password": "y0u_c4n't_gU3$$_th1s",
        "email": "testingtesting123@gmail.com",
        "address": "5555 NW Testing St\nPytest, WY 93321",
        "payment_method": "Cashier's Check"
    }
    url = '/register/'
    
    response = client.post(url, json=data)
    print(response)