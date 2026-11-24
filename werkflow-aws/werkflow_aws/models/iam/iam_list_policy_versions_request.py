from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IAMListPolicyVersionsRequest(BaseModel):
    PolicyArn: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
