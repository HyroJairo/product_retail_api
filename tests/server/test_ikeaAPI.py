class TestRegisterRoute():
    EMAIL = "testingtesting123@gmail.com"
    NAME = "Mustafa"
    PASSWORD = "y0u_c4n't_gU3$$_th1s"
    EMAIL_DICT = {"email": EMAIL}
    
    DICT = {
            "name": NAME,
            "password": PASSWORD,
            "email": EMAIL,
            "address": "5555 NW Testing St\nPytest, WY 93321",
            "payment_method": "Cashier's Check"
        }
    
    CURRENT_EMAIL_DICT = {
            "name": NAME,
            "password": PASSWORD,
            "current_email": EMAIL,
            "email": EMAIL,
            "address": "5555 NW Testing St\nPytest, WY 93321",
            "payment_method": "Cashier's Check"
        }

    URL = '/register/'
    
    ### POST
    
    def register_post(self, client):
        return client.post(self.URL, json=self.DICT)
    
    def test_register_post_type(self, client):
        response = self.register_post(client)
        assert(response.content_type == 'text/html; charset=utf-8')   
        
    def test_register_post_data(self, client):
        response = self.register_post(client)
        assert(response.get_data().decode('UTF-8') == 'account added')
        
    def test_register_post_exists(self, client):
        self.register_post(client)
        response = self.register_post(client)
        assert(response.get_data().decode('UTF-8') == 'email already exists')  
    
    ### PUT
    
    def register_put(self, client):
        return client.put(self.URL, json=self.CURRENT_EMAIL_DICT)
    
    def test_register_put_type(self, client):
        response = self.register_put(client)
        assert(response.content_type == 'text/html; charset=utf-8')
        
    def test_register_put_data(self, client):
        self.register_post(client)
        response = self.register_put(client)
        assert(response.get_data().decode('UTF-8') == 'account updated')
        
    def test_register_put_invalid(self, client):
        response = self.register_put(client)
        assert(response.get_data().decode('UTF-8') == 'invalid email')  
    
    ### DELETE

    def register_delete(self, client):
        return client.delete(self.URL, json=self.EMAIL_DICT)

    def test_register_delete_type(self, client):
        self.register_post(client)
        response = self.register_delete(client)
        assert(response.content_type == 'text/html; charset=utf-8')
        
    def test_register_delete_data(self, client):
        self.register_post(client)
        response = self.register_delete(client)
        assert(response.get_data().decode('UTF-8') == 'account deleted')
    
    def test_register_delete_invalid(self, client):
        response = self.register_delete(client)
        assert(response.get_data().decode('UTF-8') == 'invalid email')
        
    ### GET
    
    def test_register_get_type(self, client):
        response = client.get(self.URL)
        assert(response.content_type == 'text/html; charset=utf-8')
        
    def test_register_get_data(self, client):
        response = client.get(self.URL)
        assert(response.get_data().decode('UTF-8') == 'nothing here')
        
class TestLoginRoute():
    DICT = {
            "email": TestRegisterRoute.EMAIL,
            "password": TestRegisterRoute.PASSWORD,
        }
    
    URL = '/login/'
    
    ### POST
    
    def login_post(self, client):
        return client.post(self.URL, json=self.DICT)
    
    def register_login_post(self, client):
        TestRegisterRoute().register_post(client)
        return self.login_post(client)
    
    def test_login_post_type(self, client):
        response = self.login_post(client)
        assert(response.content_type == 'text/html; charset=utf-8')   
        
    def test_login_post_data(self, client):
        response = self.register_login_post(client)
        assert(response.get_data().decode('UTF-8') == f'Welcome {TestRegisterRoute.NAME}')
        
    def test_login_post_logged_in(self, client):
        self.register_login_post(client)
        response = self.login_post(client)
        assert(response.get_data().decode('UTF-8') == 'Already Logged In')   
        
    def test_login_post_invalid(self, client):
        response = self.login_post(client)
        assert(response.get_data().decode('UTF-8') == 'invalid')
        
class TestLogoutRoute():
    URL = '/logout/'
    
    ### POST
    
    def test_logout_post_type(self, client):
        response = client.post(self.URL)
        assert(response.content_type == 'text/html; charset=utf-8')
        
    def test_logout_post_data(self, client):
        TestLoginRoute().register_login_post(client)
        response = client.post(self.URL)
        assert(response.get_data().decode('UTF-8') == 'Logged Out')
        
    def test_logout_post_not_logged_in(self, client):
        response = client.post(self.URL)
        assert(response.get_data().decode('UTF-8') == 'Not Logged In')  