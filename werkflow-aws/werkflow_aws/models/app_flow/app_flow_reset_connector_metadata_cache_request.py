from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AppFlowResetConnectorMetadataCacheRequest(BaseModel):
    connectorProfileName: StrictStr | None = None
    connectorType: Literal['Salesforce', 'Singular', 'Slack', 'Redshift', 'S3', 'Marketo', 'Googleanalytics', 'Zendesk', 'Servicenow', 'Datadog', 'Trendmicro', 'Snowflake', 'Dynatrace', 'Infornexus', 'Amplitude', 'Veeva', 'EventBridge', 'LookoutMetrics', 'Upsolver', 'Honeycode', 'CustomerProfiles', 'SAPOData', 'CustomConnector', 'Pardot'] | None = None
    connectorEntityName: StrictStr | None = None
    entitiesPath: StrictStr | None = None
    apiVersion: StrictStr | None = None
