from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53DomainsNameserver(BaseModel):
    Name: StrictStr | None = None
    GlueIps: list[StrictStr] | None = None
