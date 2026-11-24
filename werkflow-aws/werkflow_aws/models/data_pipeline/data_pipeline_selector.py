from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_pipeline_operator import DataPipelineOperator


class DataPipelineSelector(BaseModel):
    fieldName: StrictStr | None = None
    operator: DataPipelineOperator | None = None
