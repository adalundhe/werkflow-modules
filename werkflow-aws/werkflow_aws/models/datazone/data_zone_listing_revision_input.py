from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneListingRevisionInput(BaseModel):
    identifier: StrictStr
    revision: StrictStr
