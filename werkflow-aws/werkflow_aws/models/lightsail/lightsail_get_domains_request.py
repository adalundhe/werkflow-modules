from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetDomainsRequest(BaseModel):
    pageToken: StrictStr | None = None
