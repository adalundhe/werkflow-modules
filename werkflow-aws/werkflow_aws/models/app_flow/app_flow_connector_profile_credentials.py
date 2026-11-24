from __future__ import annotations
from pydantic import BaseModel
from .app_flow_amplitude_connector_profile_credentials import AppFlowAmplitudeConnectorProfileCredentials
from .app_flow_custom_connector_profile_credentials import AppFlowCustomConnectorProfileCredentials
from .app_flow_datadog_connector_profile_credentials import AppFlowDatadogConnectorProfileCredentials
from .app_flow_dynatrace_connector_profile_credentials import AppFlowDynatraceConnectorProfileCredentials
from .app_flow_google_analytics_connector_profile_credentials import AppFlowGoogleAnalyticsConnectorProfileCredentials
from .app_flow_honeycode_connector_profile_credentials import AppFlowHoneycodeConnectorProfileCredentials
from .app_flow_infor_nexus_connector_profile_credentials import AppFlowInforNexusConnectorProfileCredentials
from .app_flow_marketo_connector_profile_credentials import AppFlowMarketoConnectorProfileCredentials
from .app_flow_pardot_connector_profile_credentials import AppFlowPardotConnectorProfileCredentials
from .app_flow_redshift_connector_profile_credentials import AppFlowRedshiftConnectorProfileCredentials
from .app_flow_sapo_data_connector_profile_credentials import AppFlowSAPODataConnectorProfileCredentials
from .app_flow_salesforce_connector_profile_credentials import AppFlowSalesforceConnectorProfileCredentials
from .app_flow_service_now_connector_profile_credentials import AppFlowServiceNowConnectorProfileCredentials
from .app_flow_singular_connector_profile_credentials import AppFlowSingularConnectorProfileCredentials
from .app_flow_slack_connector_profile_credentials import AppFlowSlackConnectorProfileCredentials
from .app_flow_snowflake_connector_profile_credentials import AppFlowSnowflakeConnectorProfileCredentials
from .app_flow_trendmicro_connector_profile_credentials import AppFlowTrendmicroConnectorProfileCredentials
from .app_flow_veeva_connector_profile_credentials import AppFlowVeevaConnectorProfileCredentials
from .app_flow_zendesk_connector_profile_credentials import AppFlowZendeskConnectorProfileCredentials


class AppFlowConnectorProfileCredentials(BaseModel):
    Amplitude: AppFlowAmplitudeConnectorProfileCredentials | None = None
    Datadog: AppFlowDatadogConnectorProfileCredentials | None = None
    Dynatrace: AppFlowDynatraceConnectorProfileCredentials | None = None
    GoogleAnalytics: AppFlowGoogleAnalyticsConnectorProfileCredentials | None = None
    Honeycode: AppFlowHoneycodeConnectorProfileCredentials | None = None
    InforNexus: AppFlowInforNexusConnectorProfileCredentials | None = None
    Marketo: AppFlowMarketoConnectorProfileCredentials | None = None
    Redshift: AppFlowRedshiftConnectorProfileCredentials | None = None
    Salesforce: AppFlowSalesforceConnectorProfileCredentials | None = None
    ServiceNow: AppFlowServiceNowConnectorProfileCredentials | None = None
    Singular: AppFlowSingularConnectorProfileCredentials | None = None
    Slack: AppFlowSlackConnectorProfileCredentials | None = None
    Snowflake: AppFlowSnowflakeConnectorProfileCredentials | None = None
    Trendmicro: AppFlowTrendmicroConnectorProfileCredentials | None = None
    Veeva: AppFlowVeevaConnectorProfileCredentials | None = None
    Zendesk: AppFlowZendeskConnectorProfileCredentials | None = None
    SAPOData: AppFlowSAPODataConnectorProfileCredentials | None = None
    CustomConnector: AppFlowCustomConnectorProfileCredentials | None = None
    Pardot: AppFlowPardotConnectorProfileCredentials | None = None
