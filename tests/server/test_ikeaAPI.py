class TestRegisterRoute():
    REGISTER_EMAIL = "testingtesting123@gmail.com"
    REGISTER_EMAIL_DICT = {"email": REGISTER_EMAIL}
    
    REGISTER_DICT = {
            "name": "Mustafa",
            "password": "y0u_c4n't_gU3$$_th1s",
            "email": REGISTER_EMAIL,
            "address": "5555 NW Testing St\nPytest, WY 93321",
            "payment_method": "Cashier's Check"
        }
    
    REGISTER_CURRENT_EMAIL_DICT = {
            "name": "Mustafa",
            "password": "y0u_c4n't_gU3$$_th1s",
            "current_email": REGISTER_EMAIL,
            "email": REGISTER_EMAIL,
            "address": "5555 NW Testing St\nPytest, WY 93321",
            "payment_method": "Cashier's Check"
        }

    REGISTER_URL = '/register/'
    
    def register_post(self, client):
        client.post(self.REGISTER_URL, json=self.REGISTER_DICT)
    
    ### POST
    
    def test_register_post_type(self, client):
        response = client.post(self.REGISTER_URL, json=self.REGISTER_DICT)
        assert(response.content_type == 'text/html; charset=utf-8')   
        
    def test_register_post_data(self, client):
        response = client.post(self.REGISTER_URL, json=self.REGISTER_DICT)
        assert(response.get_data().decode('UTF-8') == 'account added')
        
    def test_register_post_exists(self, client):
        response = client.post(self.REGISTER_URL, json=self.REGISTER_DICT)
        response = client.post(self.REGISTER_URL, json=self.REGISTER_DICT)
        assert(response.get_data().decode('UTF-8') == 'email already exists')  
    
    ### PUT
    
    def test_register_put_type(self, client):
        response = client.put(self.REGISTER_URL, json=self.REGISTER_CURRENT_EMAIL_DICT)
        assert(response.content_type == 'text/html; charset=utf-8')
        
    def test_register_put_data(self, client):
        self.register_post(client)
        response = client.put(self.REGISTER_URL, json=self.REGISTER_CURRENT_EMAIL_DICT)
        assert(response.get_data().decode('UTF-8') == 'account updated')
        
    def test_register_put_invalid(self, client):
        response = client.put(self.REGISTER_URL, json=self.REGISTER_CURRENT_EMAIL_DICT)
        assert(response.get_data().decode('UTF-8') == 'invalid email')  
    
    ### DELETE

    def test_register_delete_type(self, client):
        self.register_post(client)
        response = client.delete(self.REGISTER_URL, json=self.REGISTER_EMAIL_DICT)
        assert(response.content_type == 'text/html; charset=utf-8')
        
    def test_register_delete_data(self, client):
        self.register_post(client)
        response = client.delete(self.REGISTER_URL, json=self.REGISTER_EMAIL_DICT)
        assert(response.get_data().decode('UTF-8') == 'account deleted')
    
    def test_register_delete_invalid(self, client):
        response = client.delete(self.REGISTER_URL, json=self.REGISTER_EMAIL_DICT)
        assert(response.get_data().decode('UTF-8') == 'invalid email')