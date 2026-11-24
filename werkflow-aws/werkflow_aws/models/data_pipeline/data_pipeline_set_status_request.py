from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataPipelineSetStatusRequest(BaseModel):
    pipelineId: StrictStr
    objectIds: list[StrictStr]
    status: StrictStr
