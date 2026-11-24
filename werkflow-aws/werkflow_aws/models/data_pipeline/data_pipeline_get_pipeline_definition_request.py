from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataPipelineGetPipelineDefinitionRequest(BaseModel):
    pipelineId: StrictStr
    version: StrictStr | None = None
