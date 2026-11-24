from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataPipelineDescribePipelinesRequest(BaseModel):
    pipelineIds: list[StrictStr]
