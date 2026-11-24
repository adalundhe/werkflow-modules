from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KMSListRetirableGrantsRequest(BaseModel):
    Limit: StrictInt | None = None
    Marker: StrictStr | None = None
    RetiringPrincipal: StrictStr | None = None
    RetiringServicePrincipal: StrictStr | None = None
