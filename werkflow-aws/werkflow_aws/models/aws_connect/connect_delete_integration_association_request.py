from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteIntegrationAssociationRequest(BaseModel):
    InstanceId: StrictStr
    IntegrationAssociationId: StrictStr
