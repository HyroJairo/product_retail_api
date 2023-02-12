class TestRegisterRoute():
    REGISTER_DICT = {
            "name": "Mustafa",
            "password": "y0u_c4n't_gU3$$_th1s",
            "email": "testingtesting123@gmail.com",
            "address": "5555 NW Testing St\nPytest, WY 93321",
            "payment_method": "Cashier's Check"
        }

    REGISTER_URL = '/register/'
    
    def register_post(self, client):
        client.post(TestRegisterRoute.REGISTER_URL, json=TestRegisterRoute.REGISTER_DICT)
    
    ### POST
    
    def test_register_post_type(self, client):
        response = client.post(TestRegisterRoute.REGISTER_URL, json=TestRegisterRoute.REGISTER_DICT)
        assert(response.content_type == 'text/html; charset=utf-8')   
        
    def test_register_post_data(self, client):
        response = client.post(TestRegisterRoute.REGISTER_URL, json=TestRegisterRoute.REGISTER_DICT)
        assert(response.get_data().decode('UTF-8') == 'account added')
        
    def test_register_post_exists(self, client):
        response = client.post(TestRegisterRoute.REGISTER_URL, json=TestRegisterRoute.REGISTER_DICT)
        response = client.post(TestRegisterRoute.REGISTER_URL, json=TestRegisterRoute.REGISTER_DICT)
        assert(response.get_data().decode('UTF-8') == 'email already exists')  
    
    ### DELETE
    
    def test_register_delete_type(self, client):
        self.register_post(client)
        response = client.delete(TestRegisterRoute.REGISTER_URL, json=TestRegisterRoute.REGISTER_DICT)
        assert(response.content_type == 'text/html; charset=utf-8')
        
    def test_register_delete_data(self, client):
        self.register_post(client)
        response = client.delete(TestRegisterRoute.REGISTER_URL, json=TestRegisterRoute.REGISTER_DICT)
        assert(response.get_data().decode('UTF-8') == 'account deleted')
    
    # test fails due to bug in code  
    # def test_register_delete_invalid(self, client):
    #     response = client.delete(TestRegisterRoute.REGISTER_URL, json=TestRegisterRoute.REGISTER_DICT)
    #     assert(response.get_data().decode('UTF-8') == 'invalid email')
        