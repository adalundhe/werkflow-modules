from __future__ import annotations
from pydantic import BaseModel
from .app_flow_amplitude_source_properties import AppFlowAmplitudeSourceProperties
from .app_flow_custom_connector_source_properties import AppFlowCustomConnectorSourceProperties
from .app_flow_datadog_source_properties import AppFlowDatadogSourceProperties
from .app_flow_dynatrace_source_properties import AppFlowDynatraceSourceProperties
from .app_flow_google_analytics_source_properties import AppFlowGoogleAnalyticsSourceProperties
from .app_flow_infor_nexus_source_properties import AppFlowInforNexusSourceProperties
from .app_flow_marketo_source_properties import AppFlowMarketoSourceProperties
from .app_flow_pardot_source_properties import AppFlowPardotSourceProperties
from .app_flow_s3_source_properties import AppFlowS3SourceProperties
from .app_flow_sapo_data_source_properties import AppFlowSAPODataSourceProperties
from .app_flow_salesforce_source_properties import AppFlowSalesforceSourceProperties
from .app_flow_service_now_source_properties import AppFlowServiceNowSourceProperties
from .app_flow_singular_source_properties import AppFlowSingularSourceProperties
from .app_flow_slack_source_properties import AppFlowSlackSourceProperties
from .app_flow_trendmicro_source_properties import AppFlowTrendmicroSourceProperties
from .app_flow_veeva_source_properties import AppFlowVeevaSourceProperties
from .app_flow_zendesk_source_properties import AppFlowZendeskSourceProperties


class AppFlowSourceConnectorProperties(BaseModel):
    Amplitude: AppFlowAmplitudeSourceProperties | None = None
    Datadog: AppFlowDatadogSourceProperties | None = None
    Dynatrace: AppFlowDynatraceSourceProperties | None = None
    GoogleAnalytics: AppFlowGoogleAnalyticsSourceProperties | None = None
    InforNexus: AppFlowInforNexusSourceProperties | None = None
    Marketo: AppFlowMarketoSourceProperties | None = None
    S3: AppFlowS3SourceProperties | None = None
    Salesforce: AppFlowSalesforceSourceProperties | None = None
    ServiceNow: AppFlowServiceNowSourceProperties | None = None
    Singular: AppFlowSingularSourceProperties | None = None
    Slack: AppFlowSlackSourceProperties | None = None
    Trendmicro: AppFlowTrendmicroSourceProperties | None = None
    Veeva: AppFlowVeevaSourceProperties | None = None
    Zendesk: AppFlowZendeskSourceProperties | None = None
    SAPOData: AppFlowSAPODataSourceProperties | None = None
    CustomConnector: AppFlowCustomConnectorSourceProperties | None = None
    Pardot: AppFlowPardotSourceProperties | None = None
