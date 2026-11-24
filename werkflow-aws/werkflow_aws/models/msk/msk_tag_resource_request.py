from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKTagResourceRequest(BaseModel):
    ResourceArn: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
