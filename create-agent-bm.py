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

"""This code creates a Business Messages agent.

Read more: https://developers.google.com/business-communications/business-messages/guides/how-to/agents?method=api#create_the_agent

This code is based on the https://github.com/google-business-communications/python-businessmessages
Python Business Messages client library.
"""

from oauth2client.service_account import ServiceAccountCredentials
from businesscommunications.businesscommunications_v1_client import BusinesscommunicationsV1
from businesscommunications.businesscommunications_v1_messages import (
    Agent, BusinesscommunicationsBrandsAgentsCreateRequest,
    BusinessMessagesAgent, BusinessMessagesEntryPointConfig,
    ContactOption, ConversationalSetting, ConversationStarters,
    Hours, HumanRepresentative, MessagingAvailability,
    NonLocalConfig, Phone, PrivacyPolicy, Suggestion,
    SuggestedReply, SupportedAgentInteraction,
    TimeOfDay, WelcomeMessage
)

# Edit the values below:
BRAND_ID = 'EDIT_HERE'
SCOPES = ['https://www.googleapis.com/auth/businesscommunications']
SERVICE_ACCOUNT_FILE = './service_account_key.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

client = BusinesscommunicationsV1(credentials=credentials)

agents_service = BusinesscommunicationsV1.BrandsAgentsService(client)

brand_name = 'brands/ '+ BRAND_ID

agent = Agent(
    displayName='My first agent',
    businessMessagesAgent=BusinessMessagesAgent(
        customAgentId='CUSTOM_ID', # Optional
        logoUrl='https://developers.google.com/identity/images/g-logo.png',
        entryPointConfigs=[BusinessMessagesEntryPointConfig(
            allowedEntryPoint=BusinessMessagesEntryPointConfig.AllowedEntryPointValueValuesEnum.LOCATION
        ), BusinessMessagesEntryPointConfig(
            allowedEntryPoint=BusinessMessagesEntryPointConfig.AllowedEntryPointValueValuesEnum.NON_LOCAL
        )],
        nonLocalConfig=NonLocalConfig(
            # List of phone numbers for call deflection, values must be globally unique
            # Generating a random phone number for demonstration purposes
            # This should be replaced with a real brand phone number
            callDeflectionPhoneNumbers=[Phone(number='+10000000000'),
              Phone(number='+10000000001')],
            # Contact information for the agent that displays with the messaging button
            contactOption=ContactOption(
                    options=[ContactOption.OptionsValueListEntryValuesEnum.EMAIL,
                        ContactOption.OptionsValueListEntryValuesEnum.PHONE],
                    url='https://www.your-company-website.com'
                ),
            # Domains enabled for messaging within Search, values must be globally unique
            # Generating a random URL for demonstration purposes
            # This should be replaced with a real brand URL
            enabledDomains=['your-company-website.com'],
            # Agent's phone number. Overrides the `phone` field for conversations started from non-local entry points
            phoneNumber=Phone(number='+10000000000'),
            # List of CLDR region codes for countries where the agent is allowed to launch `NON_LOCAL` entry points.
            # Example is for launching in Canada and the USA
            regionCodes=['US', 'CA']
        ),
        defaultLocale='en',
        conversationalSettings=BusinessMessagesAgent.ConversationalSettingsValue(
            additionalProperties=[BusinessMessagesAgent.ConversationalSettingsValue.AdditionalProperty(
                key='en',
                value=ConversationalSetting(
                    privacyPolicy=PrivacyPolicy(url='https://www.your-company-website.com/privacy'),
                    welcomeMessage=WelcomeMessage(text='This is a sample welcome message'),
                    conversationStarters=[
                        ConversationStarters(
                            suggestion=Suggestion(
                                reply=SuggestedReply(text='Option 1',
                                                     postbackData='postback_option_1')
                            )
                        )
                    ]
                )
            )]
        ),
        primaryAgentInteraction=SupportedAgentInteraction(
            interactionType=SupportedAgentInteraction.InteractionTypeValueValuesEnum.HUMAN,
            humanRepresentative=HumanRepresentative(
                humanMessagingAvailability=MessagingAvailability(hours=[
                        Hours(
                            startTime=TimeOfDay(hours=8, minutes=30),
                            startDay=Hours.StartDayValueValuesEnum.MONDAY,
                            endDay=Hours.EndDayValueValuesEnum.SATURDAY,
                            endTime=TimeOfDay(hours=20, minutes=0),
                            timeZone='America/Los_Angeles'
                        )
                    ])
            )
        ),
    )
)

new_agent = agents_service.Create(
    BusinesscommunicationsBrandsAgentsCreateRequest(
        agent=agent,
        parent=brand_name
    )
)

print(new_agent)
