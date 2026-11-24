from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class AppFlowListConnectorEntitiesRequest(BaseModel):
    connectorProfileName: StrictStr | None = None
    connectorType: Literal['Salesforce', 'Singular', 'Slack', 'Redshift', 'S3', 'Marketo', 'Googleanalytics', 'Zendesk', 'Servicenow', 'Datadog', 'Trendmicro', 'Snowflake', 'Dynatrace', 'Infornexus', 'Amplitude', 'Veeva', 'EventBridge', 'LookoutMetrics', 'Upsolver', 'Honeycode', 'CustomerProfiles', 'SAPOData', 'CustomConnector', 'Pardot'] | None = None
    entitiesPath: StrictStr | None = None
    apiVersion: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
