from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteUseCaseRequest(BaseModel):
    InstanceId: StrictStr
    IntegrationAssociationId: StrictStr
    UseCaseId: StrictStr
