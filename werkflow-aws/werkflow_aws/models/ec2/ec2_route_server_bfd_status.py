from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2RouteServerBfdStatus(BaseModel):
    Status: StrictStr | None = None
