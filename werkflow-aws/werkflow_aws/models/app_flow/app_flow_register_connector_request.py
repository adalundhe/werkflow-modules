from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .app_flow_connector_provisioning_config import AppFlowConnectorProvisioningConfig


class AppFlowRegisterConnectorRequest(BaseModel):
    connectorLabel: StrictStr | None = None
    description: StrictStr | None = None
    connectorProvisioningType: Literal['LAMBDA'] | None = None
    connectorProvisioningConfig: AppFlowConnectorProvisioningConfig | None = None
    clientToken: StrictStr | None = None
