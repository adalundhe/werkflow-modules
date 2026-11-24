from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .app_flow_connector_profile_properties import AppFlowConnectorProfileProperties
from .app_flow_private_connection_provisioning_state import AppFlowPrivateConnectionProvisioningState


class AppFlowConnectorProfile(BaseModel):
    connectorProfileArn: StrictStr | None = None
    connectorProfileName: StrictStr | None = None
    connectorType: StrictStr | None = None
    connectorLabel: StrictStr | None = None
    connectionMode: StrictStr | None = None
    credentialsArn: StrictStr | None = None
    connectorProfileProperties: AppFlowConnectorProfileProperties | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    privateConnectionProvisioningState: AppFlowPrivateConnectionProvisioningState | None = None
