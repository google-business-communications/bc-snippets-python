## Copyright 2022 Google LLC
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##     https://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.

"""This code snippet lists all greetings associated with an agent

Read more: https://developers.google.com/business-communications/business-messages/reference/business-communications/rest/v1/brands.agents.greetings/list

This code is based on the https://github.com/google-business-communications/python-businessmessages
Python Business Messages client library.
"""

from oauth2client.service_account import ServiceAccountCredentials
from businesscommunications.businesscommunications_v1_client import BusinesscommunicationsV1
from businesscommunications.businesscommunications_v1_messages import (
    BusinesscommunicationsBrandsAgentsGreetingsListRequest,
)

# Edit the values below:
BRAND_ID = 'EDIT_HERE'
AGENT_ID = 'EDIT_HERE'

SCOPES = ['https://www.googleapis.com/auth/businesscommunications']
SERVICE_ACCOUNT_FILE = './service_account_key.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

client = BusinesscommunicationsV1(credentials=credentials)

agent_name = 'brands/' + BRAND_ID + '/agents/' + AGENT_ID

greetings_service = BusinesscommunicationsV1.BrandsAgentsGreetingsService(client)

greetings = greetings_service.List(
    BusinesscommunicationsBrandsAgentsGreetingsListRequest(parent=agent_name))

print(greetings)

greetings_service = BusinesscommunicationsV1.BrandsAgentsGreetingsService(client)
