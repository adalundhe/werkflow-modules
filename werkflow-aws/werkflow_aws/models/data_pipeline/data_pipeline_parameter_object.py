from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_pipeline_parameter_attribute import DataPipelineParameterAttribute


class DataPipelineParameterObject(BaseModel):
    id: StrictStr | None = None
    attributes: list[DataPipelineParameterAttribute] | None = None
