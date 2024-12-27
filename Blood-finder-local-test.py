from mira_sdk import MiraClient, CompoundFlow
from mira_sdk.exceptions import FlowError

# Initialize Mira Client with your API Key
client = MiraClient(config={"API_KEY": "sb-f915fc31d83eed93780402d2eec45787"})

# Load the blood bank locator AI flow configuration
flow = CompoundFlow(source="flow.yaml")  # Ensure the YAML file is named and located correctly

# Prepare test inputs
test_input = {
    "blood_type": "O-negative",  # Example blood type
    "location": "Indira Gandhi Institute of Medical Sciences (IGIMS), Patna"  # Example location
}

try:
    # Test the compound flow with the inputs
    response = client.flow.test(flow, test_input)
    print("Test response:", response)  # Output the test results
except FlowError as e:
    print("Test failed:", str(e))      # Handle any errors during testing
except Exception as ex:
    print("An unexpected error occurred:", str(ex))
