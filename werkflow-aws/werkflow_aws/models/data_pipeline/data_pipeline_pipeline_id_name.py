from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataPipelinePipelineIdName(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
