from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_pipeline_tag import DataPipelineTag


class DataPipelineAddTagsRequest(BaseModel):
    pipelineId: StrictStr
    tags: list[DataPipelineTag]
