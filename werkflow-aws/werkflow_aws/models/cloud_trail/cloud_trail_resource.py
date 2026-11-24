from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailResource(BaseModel):
    ResourceType: StrictStr | None = None
    ResourceName: StrictStr | None = None
