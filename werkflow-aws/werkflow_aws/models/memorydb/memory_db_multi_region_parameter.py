from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MemoryDBMultiRegionParameter(BaseModel):
    Name: StrictStr | None = None
    Value: StrictStr | None = None
    Description: StrictStr | None = None
    Source: StrictStr | None = None
    DataType: StrictStr | None = None
    AllowedValues: StrictStr | None = None
    MinimumEngineVersion: StrictStr | None = None
