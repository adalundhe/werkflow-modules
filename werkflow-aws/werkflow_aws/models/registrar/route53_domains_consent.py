from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class Route53DomainsConsent(BaseModel):
    MaxPrice: StrictFloat | StrictInt
    Currency: StrictStr
