from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DMSDescribeEndpointSettingsRequest(BaseModel):
    EngineName: StrictStr
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
