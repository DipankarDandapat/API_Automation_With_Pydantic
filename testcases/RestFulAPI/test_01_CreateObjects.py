import json
import os

from API_Utilities import logger_utility
from API_Utilities.shared_state import shared_data

from models.create_object_model import MacBookRequest, MacBookResponse

log = logger_utility.customLogger()




payload = {
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}

headers = {
  'Content-Type': 'application/json'
}


def test_create_object(setup_env, api_client, env):

    log.info(f"Running test in environment: {env}")

    payload1 = MacBookRequest(**payload)

    baseURL = os.getenv('BASEURL')

    response = api_client.post_request(base_url =baseURL, api_endpoint="/objects",payload=payload1.model_dump(),header=headers)

    assert response.status_code == 200, "Unexpected status code: " + str(response.status_code)

    responsedata=response.json()

    MacBookResponse.model_validate_json(response.text)

    api_response=MacBookResponse(**responsedata)

    shared_data['test_create_object'] = {"id": responsedata['id']}












