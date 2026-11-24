from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailDeleteSubdomainRequest(BaseModel):
    subdomainName: StrictStr
