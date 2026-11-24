from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataPipelineRemoveTagsRequest(BaseModel):
    pipelineId: StrictStr
    tagKeys: list[StrictStr]
