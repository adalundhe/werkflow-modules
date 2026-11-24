from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneSubscribedListingInput(BaseModel):
    identifier: StrictStr
