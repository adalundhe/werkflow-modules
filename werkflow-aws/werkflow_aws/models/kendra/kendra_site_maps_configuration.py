from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraSiteMapsConfiguration(BaseModel):
    SiteMaps: list[StrictStr] | None = None
