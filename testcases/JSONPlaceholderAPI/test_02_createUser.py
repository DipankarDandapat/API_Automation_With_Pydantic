import os
from API_Utilities import logger_utility
from models.user_models import NewUser ,UserCreate

log = logger_utility.customLogger()


def test_create_users(setup_env, api_client, env):

    log.info(f"Running test in environment: {env}")

    baseURL = os.getenv('JSONPLACEHOLDER_URL')

    new_user = NewUser(
        name="dipak",
        username="dipak",
        email="dipak@example.com"
    )

    headers = {
        'Content-Type': 'application/json'
    }

    response = api_client.post_request(base_url =baseURL, api_endpoint="/users",payload=new_user.model_dump(),header=headers)

    assert response.status_code == 201, "Unexpected status code: " + str(response.status_code)

    responsedata = response.json()
    created_user = UserCreate(**responsedata)  # Validate response schema
    assert created_user.name == new_user.name
    assert created_user.email == new_user.email


