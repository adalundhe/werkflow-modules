from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetDisksRequest(BaseModel):
    pageToken: StrictStr | None = None
