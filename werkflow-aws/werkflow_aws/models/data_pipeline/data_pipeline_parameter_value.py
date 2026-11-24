from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataPipelineParameterValue(BaseModel):
    id: StrictStr | None = None
    stringValue: StrictStr | None = None
