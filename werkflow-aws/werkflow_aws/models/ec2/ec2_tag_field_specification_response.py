from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2TagFieldSpecificationResponse(BaseModel):
    ResourceType: StrictStr | None = None
    TagKeys: list[StrictStr] | None = None
