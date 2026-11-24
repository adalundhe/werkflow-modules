from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneAthenaPropertiesInput(BaseModel):
    workgroupName: StrictStr | None = None
