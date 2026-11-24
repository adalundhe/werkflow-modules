from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .data_pipeline_task_object import DataPipelineTaskObject


class DataPipelinePollForTaskResponse(BaseModel):
    taskObject: DataPipelineTaskObject | None = None
    ResponseMetadata: dict[str, Any] | None = None
