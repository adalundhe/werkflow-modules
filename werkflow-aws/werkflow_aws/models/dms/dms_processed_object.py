from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSProcessedObject(BaseModel):
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    EndpointType: StrictStr | None = None
