from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneCloudFormationProperties(BaseModel):
    templateUrl: StrictStr | None = None
