from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .quick_sight_auth_config import QuickSightAuthConfig
from .quick_sight_resource_permission import QuickSightResourcePermission
from .quick_sight_tag import QuickSightTag


class QuickSightCreateActionConnectorRequest(BaseModel):
    AwsAccountId: StrictStr
    ActionConnectorId: StrictStr
    Name: StrictStr
    Type: Literal['GENERIC_HTTP', 'SERVICENOW_NOW_PLATFORM', 'SALESFORCE_CRM', 'MICROSOFT_OUTLOOK', 'PAGERDUTY_ADVANCE', 'JIRA_CLOUD', 'ATLASSIAN_CONFLUENCE', 'AMAZON_S3', 'AMAZON_BEDROCK_AGENT_RUNTIME', 'AMAZON_BEDROCK_RUNTIME', 'AMAZON_BEDROCK_DATA_AUTOMATION_RUNTIME', 'AMAZON_TEXTRACT', 'AMAZON_COMPREHEND', 'AMAZON_COMPREHEND_MEDICAL', 'MICROSOFT_ONEDRIVE', 'MICROSOFT_SHAREPOINT', 'MICROSOFT_TEAMS', 'SAP_BUSINESSPARTNER', 'SAP_PRODUCTMASTERDATA', 'SAP_PHYSICALINVENTORY', 'SAP_BILLOFMATERIALS', 'SAP_MATERIALSTOCK', 'ZENDESK_SUITE', 'SMARTSHEET', 'SLACK', 'ASANA', 'BAMBOO_HR']
    AuthenticationConfig: QuickSightAuthConfig
    Description: StrictStr | None = None
    Permissions: list[QuickSightResourcePermission] | None = None
    VpcConnectionArn: StrictStr | None = None
    Tags: list[QuickSightTag] | None = None
