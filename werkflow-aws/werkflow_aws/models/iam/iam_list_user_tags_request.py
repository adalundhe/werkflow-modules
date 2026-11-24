from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IAMListUserTagsRequest(BaseModel):
    UserName: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
