from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneAthenaPropertiesOutput(BaseModel):
    workgroupName: StrictStr | None = None
