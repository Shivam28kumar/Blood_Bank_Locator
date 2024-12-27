from mira_sdk import MiraClient, Flow, CompoundFlow
from mira_sdk.exceptions import FlowError
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# api_key = os.getenv("API_KEY")

# Initialize the client
client = MiraClient(config={"API_KEY": "sb-f915fc31d83eed93780402d2eec45787"})

# Test the flow locally
flow = CompoundFlow(source="flow.yaml")
try:
	client.flow.deploy(flow)
except FlowError as e:
	print(f"Error occured: {str(e)}")