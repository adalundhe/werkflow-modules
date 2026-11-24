from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AppFlowDescribeConnectorEntityRequest(BaseModel):
    connectorEntityName: StrictStr
    connectorType: Literal['Salesforce', 'Singular', 'Slack', 'Redshift', 'S3', 'Marketo', 'Googleanalytics', 'Zendesk', 'Servicenow', 'Datadog', 'Trendmicro', 'Snowflake', 'Dynatrace', 'Infornexus', 'Amplitude', 'Veeva', 'EventBridge', 'LookoutMetrics', 'Upsolver', 'Honeycode', 'CustomerProfiles', 'SAPOData', 'CustomConnector', 'Pardot'] | None = None
    connectorProfileName: StrictStr | None = None
    apiVersion: StrictStr | None = None
