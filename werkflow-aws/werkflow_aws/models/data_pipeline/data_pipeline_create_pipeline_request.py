from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_pipeline_tag import DataPipelineTag


class DataPipelineCreatePipelineRequest(BaseModel):
    name: StrictStr
    uniqueId: StrictStr
    description: StrictStr | None = None
    tags: list[DataPipelineTag] | None = None
