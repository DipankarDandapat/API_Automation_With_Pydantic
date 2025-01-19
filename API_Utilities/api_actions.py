import json
from API_Utilities import logger_utility

log = logger_utility.customLogger()
class APIClient:
    def __init__(self,session):
        self.session = session


    def get_request(self, base_url, api_endpoint, header=None, query_params=None):
        try:
            # Log the HTTP method being used
            log.info(f"Request Method: GET")

            # Constructing the full URL
            url = f"{base_url}{api_endpoint}"


            log.info(f"Constructed URL: {url}")

            # Log query parameters if provided
            if query_params:
                log.info(f"Query Parameters: {query_params}")
            else:
                log.info("No query parameters provided.")

            # Log headers if provided
            if header:
                log.info(f"Request Headers: {header}")
            else:
                log.info("No headers provided.")

            response = self.session.get(url, headers=header, params=query_params, timeout=None)

            return response

        except Exception as e:
            log.error(f"An error occurred during the GET request: {str(e)}")
            raise



    def post_request(self, base_url, api_endpoint, header=None, param=None, payload=None, file=None):


        url = f"{base_url}{api_endpoint}"

        # Log the request type (GET, POST, PATCH, etc.)
        log.info(f"Request Type: POST")

        # Log the URL being requested
        log.info(f"Request URL: {url}")

        # Log headers if provided
        if header:
            log.info(f"Request Headers: {header}")
        else:
            log.warning(f"No headers provided.")

        # Log query params if any
        if param:
            log.info(f"Query Parameters: {param}")
        else:
            log.warning(f"No query parameters provided.")

        # Log payload if present
        if payload:
            log.info(f"Request Payload: {payload}")
        else:
            log.warning(f"No payload provided.")

        # Log if a file is being sent
        if file:
            log.info(f"File included in the request.")
        else:
            log.info(f"No file included in the request.")

        # Perform the POST request
        try:
            if file is not None:
                # When file is present, do not use json.dumps for payload
                response = self.session.post(url, headers=header, data=payload, params=param, files=file, timeout=None)
            else:
                # If no file, use json.dumps for payload
                response = self.session.post(url, headers=header, data=json.dumps(payload), params=param, timeout=None)

            return response

        except Exception as e:
            log.error(f"Error occurred during the POST request: {str(e)}")
            raise  # Reraise the exception after logging it



    def put_request(self, base_url, api_endpoint, header=None, payload=None, param=None):
        url = f"{base_url}{api_endpoint}"

        # Log the request type (GET, POST, PATCH, PUT, etc.)
        log.info(f"Request Type: PUT")

        # Log the URL being requested
        log.info(f"Request URL: {url}")

        # Log headers if provided
        if header:
            log.info(f"Request Headers: {header}")
        else:
            log.warning(f"No headers provided.")

        # Log query params if any
        if param:
            log.info(f"Query Parameters: {param}")
        else:
            log.warning(f"No query parameters provided.")

        # Log payload if provided
        if payload:
            log.info(f"Request Payload: {payload}")
        else:
            log.warning(f"No payload provided.")

        # Perform the PUT request
        try:
            response = self.session.put(url, headers=header, data=json.dumps(payload), params=param, timeout=None)
            return response

        except Exception as e:
            # Log any errors that occur during the request
            log.error(f"Error occurred during the PUT request to {url}: {str(e)}")
            raise  # Re-raise the exception after logging it


    def patch_request(self, base_url, api_endpoint, header=None, payload=None):
        url = f"{base_url}{api_endpoint}"

        # Log the request type (PATCH)
        log.info(f"Request Type: PATCH")

        # Log the URL being requested
        log.info(f"Request URL: {url}")

        # Log headers if provided
        if header:
            log.info(f"Request Headers: {header}")
        else:
            log.warning(f"No headers provided.")

        # Log payload if provided
        if payload:
            log.info(f"Request Payload: {payload}")
        else:
            log.warning(f"No payload provided.")

        # Perform the PATCH request
        try:
            response = self.session.patch(url, headers=header, data=json.dumps(payload), timeout=None)

            return response

        except Exception as e:
            # Log any errors that occur during the request
            log.error(f"Error occurred during the PATCH request to {url}: {str(e)}")
            raise  # Re-raise the exception after logging it


    def delete_request(self, base_url, api_endpoint, header=None, payload=None, query_params=None):
        url = f"{base_url}{api_endpoint}"

        # Log the request type (DELETE)
        log.info(f"Request Type: DELETE")

        # Log the URL being requested
        log.info(f"Request URL: {url}")

        # Log headers if provided
        if header:
            log.info(f"Request Headers: {header}")
        else:
            log.warning(f"No headers provided.")

        # Log payload if provided (even though DELETE requests typically don't have a body, but for completeness)
        if payload:
            log.info(f"Request Payload: {payload}")
        else:
            log.warning(f"No payload provided.")

        # Log query parameters if any
        if query_params:
            log.info(f"Query Parameters: {query_params}")
        else:
            log.warning(f"No query parameters provided.")

        # Perform the DELETE request
        try:
            response = self.session.delete(url, headers=header, params=query_params, timeout=None)

            return response

        except Exception as e:
            # Log any errors that occur during the request
            log.error(f"Error occurred during the DELETE request to {url}: {str(e)}")
            raise  # Re-raise the exception after logging it
