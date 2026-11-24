from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDescribeDomainsRequest(BaseModel):
    DomainNames: list[StrictStr]
