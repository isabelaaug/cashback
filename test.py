import unittest
from flask import Flask
from flask_restful import Api
import requests


app = Flask(__name__)
api = Api(app)
testapp = app.test_client()


class CashbackTest(unittest.TestCase):
    def test_get(self):
        """Testando o retorno de cashback da API"""
        response = requests.get("https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback", params='32596325896')
        # Confirm that the request-response cycle completed successfully.
        self.assertTrue(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
