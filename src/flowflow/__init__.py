import time
import requests
import json
import logging

class FlowFlowClient:
    def __init__(self, api_token=None, debug=False):
        if api_token is None:
            raise ValueError("api_token must be supplied during initialization")
            
        self.api_token = api_token
        self.debug = debug
        self.poll_max_iterations = 1000

    def start_workflow(self, data, workflow_id):
    
        if self.debug:
            host = 'http://localhost.localdomain:8000'
        else:
            host = 'https://flowflow.ai'

        # Formatting the endpoint url
        url = f"{host}/api/v1/workflow/start/{workflow_id}"

        # Making the POST request
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_token}'  # Set the Authorization header
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))

        # Raise an exception if the request was unsuccessful
        response.raise_for_status()

        data = response.json()

        print(data)

        if data['status'] != 'OK':
            raise Exception(f"Error starting workflow: {data['message']}")

        # Extracting the progress URL from the response
        progress_url = data['progress_api_url']

        # Polling the progress URL
        counter = 0

        while True:
            logging.debug("poll")

            # Polling the progress URL
            progress_response = requests.get(progress_url, headers=headers)  # Use the headers with the token

            # Raise an exception if the request was unsuccessful
            progress_response.raise_for_status()

            progress_data = progress_response.json()

            if progress_data['status'] != 'OK':
                raise Exception(f"Error starting workflow: {data['message']}")
            
            results = progress_data.get('results')

            if progress_data.get('status') == 'FINISHED':
                return results, progress_data
            else:
                # Waiting for 2 seconds before next poll
                time.sleep(2)

            counter += 1
            if counter >= self.poll_max_iterations:
                break

        progress_data['status'] = "Error"
        progress_data['message'] = f"Workflow did not finish in {self.poll_max_iterations} polls. You can change the max poll iterations using the poll_max_iterations parameter during the client initialization."

        return progress_data