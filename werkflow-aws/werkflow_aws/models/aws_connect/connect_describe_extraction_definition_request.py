from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeExtractionDefinitionRequest(BaseModel):
    InstanceId: StrictStr
    ExtractionDefinitionId: StrictStr
