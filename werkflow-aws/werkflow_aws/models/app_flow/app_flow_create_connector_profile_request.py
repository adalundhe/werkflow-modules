from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .app_flow_connector_profile_config import AppFlowConnectorProfileConfig


class AppFlowCreateConnectorProfileRequest(BaseModel):
    connectorProfileName: StrictStr
    connectorType: Literal['Salesforce', 'Singular', 'Slack', 'Redshift', 'S3', 'Marketo', 'Googleanalytics', 'Zendesk', 'Servicenow', 'Datadog', 'Trendmicro', 'Snowflake', 'Dynatrace', 'Infornexus', 'Amplitude', 'Veeva', 'EventBridge', 'LookoutMetrics', 'Upsolver', 'Honeycode', 'CustomerProfiles', 'SAPOData', 'CustomConnector', 'Pardot']
    connectionMode: Literal['Public', 'Private']
    connectorProfileConfig: AppFlowConnectorProfileConfig
    kmsArn: StrictStr | None = None
    connectorLabel: StrictStr | None = None
    clientToken: StrictStr | None = None
