from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationDataSourceConfiguration(BaseModel):
    IntendedUse: StrictStr | None = None
