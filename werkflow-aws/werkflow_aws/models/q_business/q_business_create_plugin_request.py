from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .q_business_custom_plugin_configuration import QBusinessCustomPluginConfiguration
from .q_business_plugin_auth_configuration import QBusinessPluginAuthConfiguration
from .q_business_tag import QBusinessTag


class QBusinessCreatePluginRequest(BaseModel):
    applicationId: StrictStr
    displayName: StrictStr
    type: Literal['SERVICE_NOW', 'SALESFORCE', 'JIRA', 'ZENDESK', 'CUSTOM', 'QUICKSIGHT', 'SERVICENOW_NOW_PLATFORM', 'JIRA_CLOUD', 'SALESFORCE_CRM', 'ZENDESK_SUITE', 'ATLASSIAN_CONFLUENCE', 'GOOGLE_CALENDAR', 'MICROSOFT_TEAMS', 'MICROSOFT_EXCHANGE', 'PAGERDUTY_ADVANCE', 'SMARTSHEET', 'ASANA']
    authConfiguration: QBusinessPluginAuthConfiguration
    serverUrl: StrictStr | None = None
    customPluginConfiguration: QBusinessCustomPluginConfiguration | None = None
    tags: list[QBusinessTag] | None = None
    clientToken: StrictStr | None = None
