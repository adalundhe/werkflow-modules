from __future__ import annotations
from pydantic import BaseModel
from .app_flow_custom_connector_destination_properties import AppFlowCustomConnectorDestinationProperties
from .app_flow_customer_profiles_destination_properties import AppFlowCustomerProfilesDestinationProperties
from .app_flow_event_bridge_destination_properties import AppFlowEventBridgeDestinationProperties
from .app_flow_honeycode_destination_properties import AppFlowHoneycodeDestinationProperties
from .app_flow_lookout_metrics_destination_properties import AppFlowLookoutMetricsDestinationProperties
from .app_flow_marketo_destination_properties import AppFlowMarketoDestinationProperties
from .app_flow_redshift_destination_properties import AppFlowRedshiftDestinationProperties
from .app_flow_s3_destination_properties import AppFlowS3DestinationProperties
from .app_flow_sapo_data_destination_properties import AppFlowSAPODataDestinationProperties
from .app_flow_salesforce_destination_properties import AppFlowSalesforceDestinationProperties
from .app_flow_snowflake_destination_properties import AppFlowSnowflakeDestinationProperties
from .app_flow_upsolver_destination_properties import AppFlowUpsolverDestinationProperties
from .app_flow_zendesk_destination_properties import AppFlowZendeskDestinationProperties


class AppFlowDestinationConnectorProperties(BaseModel):
    Redshift: AppFlowRedshiftDestinationProperties | None = None
    S3: AppFlowS3DestinationProperties | None = None
    Salesforce: AppFlowSalesforceDestinationProperties | None = None
    Snowflake: AppFlowSnowflakeDestinationProperties | None = None
    EventBridge: AppFlowEventBridgeDestinationProperties | None = None
    LookoutMetrics: AppFlowLookoutMetricsDestinationProperties | None = None
    Upsolver: AppFlowUpsolverDestinationProperties | None = None
    Honeycode: AppFlowHoneycodeDestinationProperties | None = None
    CustomerProfiles: AppFlowCustomerProfilesDestinationProperties | None = None
    Zendesk: AppFlowZendeskDestinationProperties | None = None
    Marketo: AppFlowMarketoDestinationProperties | None = None
    CustomConnector: AppFlowCustomConnectorDestinationProperties | None = None
    SAPOData: AppFlowSAPODataDestinationProperties | None = None
