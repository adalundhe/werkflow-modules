from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayDescribeChapCredentialsRequest(BaseModel):
    TargetARN: StrictStr
