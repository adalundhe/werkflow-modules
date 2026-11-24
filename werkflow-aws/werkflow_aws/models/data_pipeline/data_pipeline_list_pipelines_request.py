from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataPipelineListPipelinesRequest(BaseModel):
    marker: StrictStr | None = None
