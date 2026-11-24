from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_connector_config_request import EKSConnectorConfigRequest


class EKSRegisterClusterRequest(BaseModel):
    name: StrictStr
    connectorConfig: EKSConnectorConfigRequest
    clientRequestToken: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
