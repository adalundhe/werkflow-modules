from __future__ import annotations
from pydantic import BaseModel
from .data_pipeline_selector import DataPipelineSelector


class DataPipelineQuery(BaseModel):
    selectors: list[DataPipelineSelector] | None = None
