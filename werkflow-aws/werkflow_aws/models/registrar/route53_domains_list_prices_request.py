from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class Route53DomainsListPricesRequest(BaseModel):
    Tld: StrictStr | None = None
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
