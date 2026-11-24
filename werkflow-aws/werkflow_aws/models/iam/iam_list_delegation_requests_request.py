from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IAMListDelegationRequestsRequest(BaseModel):
    OwnerId: StrictStr | None = None
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
