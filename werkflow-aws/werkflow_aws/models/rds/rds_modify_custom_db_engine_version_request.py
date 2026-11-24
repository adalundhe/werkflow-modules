from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class RDSModifyCustomDBEngineVersionRequest(BaseModel):
    Engine: StrictStr
    EngineVersion: StrictStr
    Description: StrictStr | None = None
    Status: Literal['available', 'inactive', 'inactive-except-restore'] | None = None
