from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_flow_connector_provisioning_config import AppFlowConnectorProvisioningConfig


class AppFlowUpdateConnectorRegistrationRequest(BaseModel):
    connectorLabel: StrictStr
    description: StrictStr | None = None
    connectorProvisioningConfig: AppFlowConnectorProvisioningConfig | None = None
    clientToken: StrictStr | None = None
