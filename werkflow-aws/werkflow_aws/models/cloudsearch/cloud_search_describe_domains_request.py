from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudSearchDescribeDomainsRequest(BaseModel):
    DomainNames: list[StrictStr] | None = None
