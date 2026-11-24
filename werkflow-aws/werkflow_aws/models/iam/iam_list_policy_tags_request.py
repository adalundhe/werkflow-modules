from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IAMListPolicyTagsRequest(BaseModel):
    PolicyArn: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
