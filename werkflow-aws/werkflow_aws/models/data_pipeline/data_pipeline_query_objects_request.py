from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .data_pipeline_query import DataPipelineQuery


class DataPipelineQueryObjectsRequest(BaseModel):
    pipelineId: StrictStr
    sphere: StrictStr
    query: DataPipelineQuery | None = None
    marker: StrictStr | None = None
    limit: StrictInt | None = None
