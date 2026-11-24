from __future__ import annotations
from pydantic import BaseModel
from .app_flow_amplitude_metadata import AppFlowAmplitudeMetadata
from .app_flow_customer_profiles_metadata import AppFlowCustomerProfilesMetadata
from .app_flow_datadog_metadata import AppFlowDatadogMetadata
from .app_flow_dynatrace_metadata import AppFlowDynatraceMetadata
from .app_flow_event_bridge_metadata import AppFlowEventBridgeMetadata
from .app_flow_google_analytics_metadata import AppFlowGoogleAnalyticsMetadata
from .app_flow_honeycode_metadata import AppFlowHoneycodeMetadata
from .app_flow_infor_nexus_metadata import AppFlowInforNexusMetadata
from .app_flow_marketo_metadata import AppFlowMarketoMetadata
from .app_flow_pardot_metadata import AppFlowPardotMetadata
from .app_flow_redshift_metadata import AppFlowRedshiftMetadata
from .app_flow_s3_metadata import AppFlowS3Metadata
from .app_flow_sapo_data_metadata import AppFlowSAPODataMetadata
from .app_flow_salesforce_metadata import AppFlowSalesforceMetadata
from .app_flow_service_now_metadata import AppFlowServiceNowMetadata
from .app_flow_singular_metadata import AppFlowSingularMetadata
from .app_flow_slack_metadata import AppFlowSlackMetadata
from .app_flow_snowflake_metadata import AppFlowSnowflakeMetadata
from .app_flow_trendmicro_metadata import AppFlowTrendmicroMetadata
from .app_flow_upsolver_metadata import AppFlowUpsolverMetadata
from .app_flow_veeva_metadata import AppFlowVeevaMetadata
from .app_flow_zendesk_metadata import AppFlowZendeskMetadata


class AppFlowConnectorMetadata(BaseModel):
    Amplitude: AppFlowAmplitudeMetadata | None = None
    Datadog: AppFlowDatadogMetadata | None = None
    Dynatrace: AppFlowDynatraceMetadata | None = None
    GoogleAnalytics: AppFlowGoogleAnalyticsMetadata | None = None
    InforNexus: AppFlowInforNexusMetadata | None = None
    Marketo: AppFlowMarketoMetadata | None = None
    Redshift: AppFlowRedshiftMetadata | None = None
    S3: AppFlowS3Metadata | None = None
    Salesforce: AppFlowSalesforceMetadata | None = None
    ServiceNow: AppFlowServiceNowMetadata | None = None
    Singular: AppFlowSingularMetadata | None = None
    Slack: AppFlowSlackMetadata | None = None
    Snowflake: AppFlowSnowflakeMetadata | None = None
    Trendmicro: AppFlowTrendmicroMetadata | None = None
    Veeva: AppFlowVeevaMetadata | None = None
    Zendesk: AppFlowZendeskMetadata | None = None
    EventBridge: AppFlowEventBridgeMetadata | None = None
    Upsolver: AppFlowUpsolverMetadata | None = None
    CustomerProfiles: AppFlowCustomerProfilesMetadata | None = None
    Honeycode: AppFlowHoneycodeMetadata | None = None
    SAPOData: AppFlowSAPODataMetadata | None = None
    Pardot: AppFlowPardotMetadata | None = None
