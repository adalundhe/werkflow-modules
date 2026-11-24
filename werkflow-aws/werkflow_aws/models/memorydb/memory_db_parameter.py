from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MemoryDBParameter(BaseModel):
    Name: StrictStr | None = None
    Value: StrictStr | None = None
    Description: StrictStr | None = None
    DataType: StrictStr | None = None
    AllowedValues: StrictStr | None = None
    MinimumEngineVersion: StrictStr | None = None
