import json
import os

from API_Utilities import logger_utility
from API_Utilities.shared_state import shared_data
from models.update_object_model import updateObjectPayloadModel, updateObjectResponseModel

log = logger_utility.customLogger()

payload = {
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
   }
}

headers = {
  'Content-Type': 'application/json'
}



def test_update_object(setup_env, api_client, env):

   getId = shared_data.get('test_create_object')['id']

   payload1 = updateObjectPayloadModel(**payload)


   baseURL = os.getenv('BASEURL')

   response = api_client.put_request(base_url =baseURL, api_endpoint=f"/objects/{getId}",payload=payload1.model_dump(),header=headers)

   assert response.status_code == 200, "Unexpected status code: " + str(response.status_code)

   responsedata=response.json()

   updateObjectResponseModel(**responsedata)



