from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_pipeline_pipeline_object import DataPipelinePipelineObject


class DataPipelineTaskObject(BaseModel):
    taskId: StrictStr | None = None
    pipelineId: StrictStr | None = None
    attemptId: StrictStr | None = None
    objects: dict[StrictStr, DataPipelinePipelineObject] | None = None
