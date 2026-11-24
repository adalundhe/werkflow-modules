from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityLakeDeleteCustomLogSourceRequest(BaseModel):
    sourceName: StrictStr
    sourceVersion: StrictStr | None = None
