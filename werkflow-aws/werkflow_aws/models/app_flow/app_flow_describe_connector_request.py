from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AppFlowDescribeConnectorRequest(BaseModel):
    connectorType: Literal['Salesforce', 'Singular', 'Slack', 'Redshift', 'S3', 'Marketo', 'Googleanalytics', 'Zendesk', 'Servicenow', 'Datadog', 'Trendmicro', 'Snowflake', 'Dynatrace', 'Infornexus', 'Amplitude', 'Veeva', 'EventBridge', 'LookoutMetrics', 'Upsolver', 'Honeycode', 'CustomerProfiles', 'SAPOData', 'CustomConnector', 'Pardot']
    connectorLabel: StrictStr | None = None
