from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetSubdomainsRequest(BaseModel):
    subdomainName: StrictStr | None = None
    pageToken: StrictStr | None = None
