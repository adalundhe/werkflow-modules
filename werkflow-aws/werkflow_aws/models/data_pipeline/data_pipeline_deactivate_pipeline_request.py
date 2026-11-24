from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DataPipelineDeactivatePipelineRequest(BaseModel):
    pipelineId: StrictStr
    cancelActive: StrictBool | None = None
