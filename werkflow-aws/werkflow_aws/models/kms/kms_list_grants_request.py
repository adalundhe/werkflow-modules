from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KMSListGrantsRequest(BaseModel):
    KeyId: StrictStr
    Limit: StrictInt | None = None
    Marker: StrictStr | None = None
    GrantId: StrictStr | None = None
    GranteePrincipal: StrictStr | None = None
    GranteeServicePrincipal: StrictStr | None = None
