from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IAMListMFADeviceTagsRequest(BaseModel):
    SerialNumber: StrictStr
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
