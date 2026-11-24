from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_pipeline_field import DataPipelineField
from .data_pipeline_tag import DataPipelineTag


class DataPipelinePipelineDescription(BaseModel):
    pipelineId: StrictStr | None = None
    name: StrictStr | None = None
    fields: list[DataPipelineField] | None = None
    description: StrictStr | None = None
    tags: list[DataPipelineTag] | None = None
