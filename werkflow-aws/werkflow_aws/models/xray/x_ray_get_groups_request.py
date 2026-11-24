from __future__ import annotations
from pydantic import BaseModel, StrictStr


class XRayGetGroupsRequest(BaseModel):
    NextToken: StrictStr | None = None
