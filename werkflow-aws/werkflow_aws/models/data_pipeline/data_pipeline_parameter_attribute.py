from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataPipelineParameterAttribute(BaseModel):
    key: StrictStr | None = None
    stringValue: StrictStr | None = None
