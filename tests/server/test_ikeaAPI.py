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
    
    def register_post(self, client):
        client.post(self.URL, json=self.DICT)
    
    ### POST
    
    def test_register_post_type(self, client):
        response = client.post(self.URL, json=self.DICT)
        assert(response.content_type == 'text/html; charset=utf-8')   
        
    def test_register_post_data(self, client):
        response = client.post(self.URL, json=self.DICT)
        assert(response.get_data().decode('UTF-8') == 'account added')
        
    def test_register_post_exists(self, client):
        response = client.post(self.URL, json=self.DICT)
        response = client.post(self.URL, json=self.DICT)
        assert(response.get_data().decode('UTF-8') == 'email already exists')  
    
    ### PUT
    
    def test_register_put_type(self, client):
        response = client.put(self.URL, json=self.CURRENT_EMAIL_DICT)
        assert(response.content_type == 'text/html; charset=utf-8')
        
    def test_register_put_data(self, client):
        self.register_post(client)
        response = client.put(self.URL, json=self.CURRENT_EMAIL_DICT)
        assert(response.get_data().decode('UTF-8') == 'account updated')
        
    def test_register_put_invalid(self, client):
        response = client.put(self.URL, json=self.CURRENT_EMAIL_DICT)
        assert(response.get_data().decode('UTF-8') == 'invalid email')  
    
    ### DELETE

    def test_register_delete_type(self, client):
        self.register_post(client)
        response = client.delete(self.URL, json=self.EMAIL_DICT)
        assert(response.content_type == 'text/html; charset=utf-8')
        
    def test_register_delete_data(self, client):
        self.register_post(client)
        response = client.delete(self.URL, json=self.EMAIL_DICT)
        assert(response.get_data().decode('UTF-8') == 'account deleted')
    
    def test_register_delete_invalid(self, client):
        response = client.delete(self.URL, json=self.EMAIL_DICT)
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
    
    def test_login_post_type(self, client):
        response = client.post(self.URL, json=self.DICT)
        assert(response.content_type == 'text/html; charset=utf-8')   
        
    def test_login_post_data(self, client):
        TestRegisterRoute.register_post(TestRegisterRoute, client)
        response = client.post(self.URL, json=self.DICT)
        assert(response.get_data().decode('UTF-8') == f'Welcome {TestRegisterRoute.NAME}')
        
    def test_login_post_logged_in(self, client):
        TestRegisterRoute.register_post(TestRegisterRoute, client)
        client.post(self.URL, json=self.DICT)
        response = client.post(self.URL, json=self.DICT)
        assert(response.get_data().decode('UTF-8') == 'Already Logged In')   
        
    def test_login_post_invalid(self, client):
        response = client.post(self.URL, json=self.DICT)
        assert(response.get_data().decode('UTF-8') == 'invalid')
        
# class TestLogoutoute():
#     DICT = {
#             "email": TestRegisterRoute.EMAIL,
#             "password": TestRegisterRoute.PASSWORD,
#         }
    
#     URL = '/login/'
    
#     ### POST
    
#     def test_login_post_type(self, client):
#         response = client.post(self.URL, json=self.DICT)
#         assert(response.content_type == 'text/html; charset=utf-8')   
        
#     def test_login_post_data(self, client):
#         TestRegisterRoute.register_post(TestRegisterRoute, client)
#         response = client.post(self.URL, json=self.DICT)
#         assert(response.get_data().decode('UTF-8') == f'Welcome {TestRegisterRoute.NAME}')
        
#     def test_login_post_invalid(self, client):
#         response = client.post(self.URL, json=self.DICT)
#         assert(response.get_data().decode('UTF-8') == 'invalid')  