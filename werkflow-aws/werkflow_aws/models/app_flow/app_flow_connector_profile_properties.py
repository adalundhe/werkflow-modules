from __future__ import annotations
from pydantic import BaseModel
from .app_flow_amplitude_connector_profile_properties import AppFlowAmplitudeConnectorProfileProperties
from .app_flow_custom_connector_profile_properties import AppFlowCustomConnectorProfileProperties
from .app_flow_datadog_connector_profile_properties import AppFlowDatadogConnectorProfileProperties
from .app_flow_dynatrace_connector_profile_properties import AppFlowDynatraceConnectorProfileProperties
from .app_flow_google_analytics_connector_profile_properties import AppFlowGoogleAnalyticsConnectorProfileProperties
from .app_flow_honeycode_connector_profile_properties import AppFlowHoneycodeConnectorProfileProperties
from .app_flow_infor_nexus_connector_profile_properties import AppFlowInforNexusConnectorProfileProperties
from .app_flow_marketo_connector_profile_properties import AppFlowMarketoConnectorProfileProperties
from .app_flow_pardot_connector_profile_properties import AppFlowPardotConnectorProfileProperties
from .app_flow_redshift_connector_profile_properties import AppFlowRedshiftConnectorProfileProperties
from .app_flow_sapo_data_connector_profile_properties import AppFlowSAPODataConnectorProfileProperties
from .app_flow_salesforce_connector_profile_properties import AppFlowSalesforceConnectorProfileProperties
from .app_flow_service_now_connector_profile_properties import AppFlowServiceNowConnectorProfileProperties
from .app_flow_singular_connector_profile_properties import AppFlowSingularConnectorProfileProperties
from .app_flow_slack_connector_profile_properties import AppFlowSlackConnectorProfileProperties
from .app_flow_snowflake_connector_profile_properties import AppFlowSnowflakeConnectorProfileProperties
from .app_flow_trendmicro_connector_profile_properties import AppFlowTrendmicroConnectorProfileProperties
from .app_flow_veeva_connector_profile_properties import AppFlowVeevaConnectorProfileProperties
from .app_flow_zendesk_connector_profile_properties import AppFlowZendeskConnectorProfileProperties


class AppFlowConnectorProfileProperties(BaseModel):
    Amplitude: AppFlowAmplitudeConnectorProfileProperties | None = None
    Datadog: AppFlowDatadogConnectorProfileProperties | None = None
    Dynatrace: AppFlowDynatraceConnectorProfileProperties | None = None
    GoogleAnalytics: AppFlowGoogleAnalyticsConnectorProfileProperties | None = None
    Honeycode: AppFlowHoneycodeConnectorProfileProperties | None = None
    InforNexus: AppFlowInforNexusConnectorProfileProperties | None = None
    Marketo: AppFlowMarketoConnectorProfileProperties | None = None
    Redshift: AppFlowRedshiftConnectorProfileProperties | None = None
    Salesforce: AppFlowSalesforceConnectorProfileProperties | None = None
    ServiceNow: AppFlowServiceNowConnectorProfileProperties | None = None
    Singular: AppFlowSingularConnectorProfileProperties | None = None
    Slack: AppFlowSlackConnectorProfileProperties | None = None
    Snowflake: AppFlowSnowflakeConnectorProfileProperties | None = None
    Trendmicro: AppFlowTrendmicroConnectorProfileProperties | None = None
    Veeva: AppFlowVeevaConnectorProfileProperties | None = None
    Zendesk: AppFlowZendeskConnectorProfileProperties | None = None
    SAPOData: AppFlowSAPODataConnectorProfileProperties | None = None
    CustomConnector: AppFlowCustomConnectorProfileProperties | None = None
    Pardot: AppFlowPardotConnectorProfileProperties | None = None
