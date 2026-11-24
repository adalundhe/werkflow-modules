from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataPipelineField(BaseModel):
    key: StrictStr | None = None
    stringValue: StrictStr | None = None
    refValue: StrictStr | None = None
