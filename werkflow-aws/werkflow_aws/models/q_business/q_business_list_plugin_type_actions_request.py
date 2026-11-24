from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class QBusinessListPluginTypeActionsRequest(BaseModel):
    pluginType: Literal['SERVICE_NOW', 'SALESFORCE', 'JIRA', 'ZENDESK', 'CUSTOM', 'QUICKSIGHT', 'SERVICENOW_NOW_PLATFORM', 'JIRA_CLOUD', 'SALESFORCE_CRM', 'ZENDESK_SUITE', 'ATLASSIAN_CONFLUENCE', 'GOOGLE_CALENDAR', 'MICROSOFT_TEAMS', 'MICROSOFT_EXCHANGE', 'PAGERDUTY_ADVANCE', 'SMARTSHEET', 'ASANA']
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
