from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneImport(BaseModel):
    name: StrictStr | None = None
    revision: StrictStr | None = None
