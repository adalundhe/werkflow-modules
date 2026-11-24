from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneSparkGlueArgs(BaseModel):
    connection: StrictStr | None = None
