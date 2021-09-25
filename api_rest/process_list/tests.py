from django.test import TestCase, Client

class ProcessListTestCase(TestCase):

    def setUp(self) :
        self.client = Client()

    def test_process_list(self):
        response = self.client.post('/api/procesar-lista/', 
            {   
                "sin clasificar": [3,5,5,6,8,3,4,4,7,7,1,1,2]
            },
            content_type="application/json"
        )
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['clasificado'], [1, 2, 3, 4, 5, 6, 7, 8, 5, 3, 4, 7, 1])