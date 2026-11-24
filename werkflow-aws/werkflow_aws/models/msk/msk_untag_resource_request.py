from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr | None = None
    TagKeys: list[StrictStr] | None = None
