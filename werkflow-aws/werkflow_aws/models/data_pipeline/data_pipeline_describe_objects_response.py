from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .data_pipeline_pipeline_object import DataPipelinePipelineObject


class DataPipelineDescribeObjectsResponse(BaseModel):
    pipelineObjects: list[DataPipelinePipelineObject] | None = None
    marker: StrictStr | None = None
    hasMoreResults: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
