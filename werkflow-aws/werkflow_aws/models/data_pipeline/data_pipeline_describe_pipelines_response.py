from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .data_pipeline_pipeline_description import DataPipelinePipelineDescription


class DataPipelineDescribePipelinesResponse(BaseModel):
    pipelineDescriptionList: list[DataPipelinePipelineDescription] | None = None
    ResponseMetadata: dict[str, Any] | None = None
