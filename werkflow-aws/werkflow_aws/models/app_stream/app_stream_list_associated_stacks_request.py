from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamListAssociatedStacksRequest(BaseModel):
    FleetName: StrictStr
    NextToken: StrictStr | None = None
