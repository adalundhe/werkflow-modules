from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetActiveNamesRequest(BaseModel):
    pageToken: StrictStr | None = None
