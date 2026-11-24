from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_pipeline_field import DataPipelineField


class DataPipelinePipelineObject(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    fields: list[DataPipelineField] | None = None
