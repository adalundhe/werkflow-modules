from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayDeleteChapCredentialsRequest(BaseModel):
    TargetARN: StrictStr
    InitiatorName: StrictStr
