from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DMSDescribeSchemasRequest(BaseModel):
    EndpointArn: StrictStr
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
