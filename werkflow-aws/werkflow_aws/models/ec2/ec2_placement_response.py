from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2PlacementResponse(BaseModel):
    GroupName: StrictStr | None = None
