from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneAthenaPropertiesPatch(BaseModel):
    workgroupName: StrictStr | None = None
