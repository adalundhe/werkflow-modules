from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneRedshiftServerlessStorage(BaseModel):
    workgroupName: StrictStr | None = None
