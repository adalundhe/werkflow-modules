from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_pipeline_field import DataPipelineField


class DataPipelineReportTaskProgressRequest(BaseModel):
    taskId: StrictStr
    fields: list[DataPipelineField] | None = None
