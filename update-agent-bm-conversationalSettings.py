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

"""This code updates the conversational settings of a Business Messages agent.

Read more: https://developers.google.com/business-communications/business-messages/reference/business-communications/rest/v1/brands.agents/patch

This code is based on the https://github.com/google-business-communications/python-businessmessages
Python Business Messages client library.
"""

from oauth2client.service_account import ServiceAccountCredentials
from businesscommunications.businesscommunications_v1_client import BusinesscommunicationsV1
from businesscommunications.businesscommunications_v1_messages import (
    Agent,
    BusinessMessagesAgent,
    ConversationStarters,
    ConversationalSetting,
    OfflineMessage,
    PrivacyPolicy,
    WelcomeMessage,
    NegativeBotFeedbackMessage,
    BusinesscommunicationsBrandsAgentsPatchRequest,
)

# Edit the values below:
BRAND_ID = 'EDIT_HERE'
AGENT_ID = 'EDIT_HERE'
SCOPES = ['https://www.googleapis.com/auth/businesscommunications']
SERVICE_ACCOUNT_FILE = './service_account_key.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

client = BusinesscommunicationsV1(credentials=credentials)

agents_service = BusinesscommunicationsV1.BrandsAgentsService(client)

agent_name = 'brands/' + BRAND_ID + '/agents/' + AGENT_ID

agent=Agent(
                businessMessagesAgent=BusinessMessagesAgent(
                        conversationalSettings=BusinessMessagesAgent.ConversationalSettingsValue(
                        additionalProperties=[BusinessMessagesAgent.ConversationalSettingsValue.AdditionalProperty(
                            key='en',
                            value=ConversationalSetting(
                                privacyPolicy=PrivacyPolicy(url='https://www.your-company-website.com/privacy'),
                                welcomeMessage=WelcomeMessage(text='Welcome to Business Messages'),
                            offlineMessage=OfflineMessage(text='This is an offline message'),
                                conversationStarters=[
                                    ConversationStarters(
                                        suggestion=Suggestion(
                                           reply=SuggestedReply(text='Option 1',
                                  postbackData='option_1')
                                        )
                                    )]
                                )
                            )
                        ]
                    )
                )
)

updated_agent = agents_service.Patch(
        BusinesscommunicationsBrandsAgentsPatchRequest(
            agent=agent,
            name=agent_name,
            updateMask='businessMessagesAgent.conversationalSettings.en'
        )
    )

print(updated_agent)
