import os
from API_Utilities import logger_utility
from models.user_models import User

log = logger_utility.customLogger()



def test_get_users(setup_env, api_client, env):

    log.info(f"Running test in environment: {env}")

    baseURL = os.getenv('JSONPLACEHOLDER_URL')

    response = api_client.get_request(base_url =baseURL, api_endpoint="/users")

    assert response.status_code == 200, "Unexpected status code: " + str(response.status_code)

    responsedata = response.json()

    users = [User(**user) for user in responsedata]  # Validate response schema
    assert len(users) > 0


