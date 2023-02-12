import sys
sys.path.insert(0, "backend/products")
import main as prd
import test_ikeaAPI

class TestProductsRoute():
    URL = '/products/'
    
    ### GET
    
    def test_products_get_type(self, client):
        response = client.get(self.URL)
        assert(response.content_type == 'text/html; charset=utf-8')
    
    def test_products_get_data(self, client):
        matches = ["90420332", "FREKVENS", "265.0", "9333523", "30180504"]
        
        prd.main()
        test_ikeaAPI.TestLoginRoute().register_login_post(client)
        response = client.get(self.URL)
        assert(all([x in response.get_data().decode('UTF-8') for x in matches]))
    
    def test_products_get_data_not_logged_in(self, client):
        response = client.get(self.URL)
        assert(response.get_data().decode('UTF-8') == 'please login at /login')
    
    ### POST - POST code not yet completed
        
# class TestProductIdRoute():
#     URL = '/products/<ID>/'
#     ID = 368814
    
#     ### GET
    
#     def test_product_id_get_type(self, client):
#         response = client.get(self.URL)
#         assert(response.content_type == 'text/html; charset=utf-8')
        
#     def test_product_id_get_data(self, client):
#         response = client.get(self.URL)
#         assert(response.get_data().decode('UTF-8') == 'nothing here')
    
#     ### POST - POST code not yet completed
    
#     ### PUT - PUT code not yet completed
    
#     ### DELETE - DELETE code not yet completed