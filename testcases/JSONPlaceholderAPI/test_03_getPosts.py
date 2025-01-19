import os
from API_Utilities import logger_utility
from models.post_models import Post

log = logger_utility.customLogger()


def test_get_posts(setup_env, api_client, env):

    log.info(f"Running test in environment: {env}")

    baseURL = os.getenv('JSONPLACEHOLDER_URL')

    response = api_client.get_request(base_url =baseURL, api_endpoint="/posts")

    assert response.status_code == 200, "Unexpected status code: " + str(response.status_code)

    responsedata = response.json()
    print(responsedata)

    posts = [Post(**post) for post in responsedata]  # Validate response schema
    assert len(posts) > 0


