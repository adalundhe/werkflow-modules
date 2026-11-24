from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSListNodegroupsResponse(BaseModel):
    nodegroups: list[StrictStr] | None = None
    nextToken: StrictStr | None = None
