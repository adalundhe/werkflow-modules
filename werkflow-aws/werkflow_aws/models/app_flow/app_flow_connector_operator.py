from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowConnectorOperator(BaseModel):
    Amplitude: StrictStr | None = None
    Datadog: StrictStr | None = None
    Dynatrace: StrictStr | None = None
    GoogleAnalytics: StrictStr | None = None
    InforNexus: StrictStr | None = None
    Marketo: StrictStr | None = None
    S3: StrictStr | None = None
    Salesforce: StrictStr | None = None
    ServiceNow: StrictStr | None = None
    Singular: StrictStr | None = None
    Slack: StrictStr | None = None
    Trendmicro: StrictStr | None = None
    Veeva: StrictStr | None = None
    Zendesk: StrictStr | None = None
    SAPOData: StrictStr | None = None
    CustomConnector: StrictStr | None = None
    Pardot: StrictStr | None = None
