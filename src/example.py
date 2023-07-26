import os

# Init FlowFlow client
from flowflow import FlowFlowClient
api_token = os.environ.get('FLOWFLOW_API_TOKEN') # https://flowflow.ai/settings/api-keys
client = FlowFlowClient(api_token)

# Start a workflow
workflow_id = "b1a51ad8-1094-474e-b59e-8b31ac7cb002" # Replace with your workflow ID

data = {
    "input": "The weather in Amsterdam is sunny.", # Replace with your input
}

results, details = client.start_workflow(data, workflow_id)

# Print the results of all nodes in the workflow that are configured to display the node results.
print(results)
