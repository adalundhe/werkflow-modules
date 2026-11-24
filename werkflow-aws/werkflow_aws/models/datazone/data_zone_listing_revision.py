from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneListingRevision(BaseModel):
    id: StrictStr | None = None
    revision: StrictStr | None = None
