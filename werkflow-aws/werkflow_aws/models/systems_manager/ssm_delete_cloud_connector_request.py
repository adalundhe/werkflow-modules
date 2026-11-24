from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMDeleteCloudConnectorRequest(BaseModel):
    CloudConnectorId: StrictStr
