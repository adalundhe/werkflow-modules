from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudSearchBuildSuggestersRequest(BaseModel):
    DomainName: StrictStr
