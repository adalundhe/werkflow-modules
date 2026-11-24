from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServiceOptions(BaseModel):
    SupportedRegions: list[StrictStr] | None = None
