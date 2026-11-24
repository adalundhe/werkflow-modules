from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .app_flow_authentication_config import AppFlowAuthenticationConfig
from .app_flow_connector_metadata import AppFlowConnectorMetadata
from .app_flow_connector_provisioning_config import AppFlowConnectorProvisioningConfig
from .app_flow_connector_runtime_setting import AppFlowConnectorRuntimeSetting
from .app_flow_data_transfer_api import AppFlowDataTransferApi


class AppFlowConnectorConfiguration(BaseModel):
    canUseAsSource: StrictBool | None = None
    canUseAsDestination: StrictBool | None = None
    supportedDestinationConnectors: list[StrictStr] | None = None
    supportedSchedulingFrequencies: list[StrictStr] | None = None
    isPrivateLinkEnabled: StrictBool | None = None
    isPrivateLinkEndpointUrlRequired: StrictBool | None = None
    supportedTriggerTypes: list[StrictStr] | None = None
    connectorMetadata: AppFlowConnectorMetadata | None = None
    connectorType: StrictStr | None = None
    connectorLabel: StrictStr | None = None
    connectorDescription: StrictStr | None = None
    connectorOwner: StrictStr | None = None
    connectorName: StrictStr | None = None
    connectorVersion: StrictStr | None = None
    connectorArn: StrictStr | None = None
    connectorModes: list[StrictStr] | None = None
    authenticationConfig: AppFlowAuthenticationConfig | None = None
    connectorRuntimeSettings: list[AppFlowConnectorRuntimeSetting] | None = None
    supportedApiVersions: list[StrictStr] | None = None
    supportedOperators: list[StrictStr] | None = None
    supportedWriteOperations: list[StrictStr] | None = None
    connectorProvisioningType: StrictStr | None = None
    connectorProvisioningConfig: AppFlowConnectorProvisioningConfig | None = None
    logoURL: StrictStr | None = None
    registeredAt: datetime.datetime | StrictStr | None = None
    registeredBy: StrictStr | None = None
    supportedDataTransferTypes: list[StrictStr] | None = None
    supportedDataTransferApis: list[AppFlowDataTransferApi] | None = None
