import sys
sys.path.insert(0, "backend/products")
import main as prd
import test_ikeaAPI

DUVHOLMEN_ID = "79291360"
DUVHOLMEN_LIST_MATCH = [DUVHOLMEN_ID, "FRÖSÖN/DUVHOLMEN", "Outdoor furniture", "70.0",   "Chair cushion, outdoor,          50x50 cm"]
ELVARLI_LIST_MATCH =   ["69157376",   "ELVARLI",          "Wardrobes",         "1231.0", "2 sections,          175x51x222-350 cm"]

class TestProductsRoute():
    URL = '/products/'
    
    ### GET
    
    def initialize_products_database_and_login(self, client):
        prd.main()
        test_ikeaAPI.TestLoginRoute().register_login_post(client)
    
    def test_products_get_type(self, client):
        self.initialize_products_database_and_login(client)
        response = client.get(self.URL)
        assert(response.content_type == 'text/html; charset=utf-8')
    
    def test_products_get_data(self, client):
        matches = [*DUVHOLMEN_LIST_MATCH, *ELVARLI_LIST_MATCH]
        
        self.initialize_products_database_and_login(client)
        response = client.get(self.URL)
        assert(all([x in response.get_data().decode('UTF-8') for x in matches]))
    
    def test_products_get_not_logged_in(self, client):
        response = client.get(self.URL)
        assert(response.get_data().decode('UTF-8') == 'please login at /login')
    
    ### POST - POST code not yet completed
        
class TestProductIdRoute():
    URL = f"/products/{DUVHOLMEN_ID}/"
    
    ### GET
    
    def initialize_database_login_and_get_url(self, client):
        TestProductsRoute().initialize_products_database_and_login(client)
        return client.get(self.URL)
    
    def test_product_id_get_type(self, client):
        response = self.initialize_database_login_and_get_url(client)
        assert(response.content_type == 'text/html; charset=utf-8')
        
    def test_product_id_get_data(self, client):
        response = self.initialize_database_login_and_get_url(client)
        assert(all([x in response.get_data().decode('UTF-8') for x in DUVHOLMEN_LIST_MATCH]))
        
    def test_products_id_get_not_logged_in(self, client):
        response = client.get(self.URL)
        assert(response.get_data().decode('UTF-8') == 'please login at /login')
    
    ### POST - POST code not yet completed
    
    ### PUT - PUT code not yet completed
    
    ### DELETE - DELETE code not yet completed