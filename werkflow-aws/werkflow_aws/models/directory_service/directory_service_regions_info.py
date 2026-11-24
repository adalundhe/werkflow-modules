from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceRegionsInfo(BaseModel):
    PrimaryRegion: StrictStr | None = None
    AdditionalRegions: list[StrictStr] | None = None
