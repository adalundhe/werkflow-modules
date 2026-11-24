from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53DomainsExtraParam(BaseModel):
    Name: StrictStr | None = None
    Value: StrictStr | None = None
