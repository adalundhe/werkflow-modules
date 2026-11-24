from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKListTagsForResourceRequest(BaseModel):
    ResourceArn: StrictStr | None = None
