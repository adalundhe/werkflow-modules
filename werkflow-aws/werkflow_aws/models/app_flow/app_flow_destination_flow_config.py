from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_flow_destination_connector_properties import AppFlowDestinationConnectorProperties


class AppFlowDestinationFlowConfig(BaseModel):
    connectorType: StrictStr | None = None
    apiVersion: StrictStr | None = None
    connectorProfileName: StrictStr | None = None
    destinationConnectorProperties: AppFlowDestinationConnectorProperties | None = None
