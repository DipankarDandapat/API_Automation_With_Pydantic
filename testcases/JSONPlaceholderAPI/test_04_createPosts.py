import os
from API_Utilities import logger_utility
from models.post_models import Post, PostCreate

log = logger_utility.customLogger()



def test_create_posts(setup_env, api_client, env):

    log.info(f"Running test in environment: {env}")

    baseURL = os.getenv('JSONPLACEHOLDER_URL')

    headers = {
        'Content-Type': 'application/json'
    }

    new_post = PostCreate(
        title="Test Post",
        body="This is a new test post.",
        userId=1
    )

    response = api_client.post_request(base_url =baseURL, api_endpoint="/posts",payload=new_post.model_dump(),header=headers)

    assert response.status_code == 201, "Unexpected status code: " + str(response.status_code)

    responsedata = response.json()
    created_post = Post(**responsedata)  # Validate response schema
    assert created_post.title == new_post.title
    assert created_post.body == new_post.body


