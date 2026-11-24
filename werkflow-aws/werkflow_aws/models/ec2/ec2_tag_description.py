from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2TagDescription(BaseModel):
    Key: StrictStr | None = None
    ResourceId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    Value: StrictStr | None = None
