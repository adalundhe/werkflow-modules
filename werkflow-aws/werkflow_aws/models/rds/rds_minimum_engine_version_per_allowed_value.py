from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSMinimumEngineVersionPerAllowedValue(BaseModel):
    AllowedValue: StrictStr | None = None
    MinimumEngineVersion: StrictStr | None = None
