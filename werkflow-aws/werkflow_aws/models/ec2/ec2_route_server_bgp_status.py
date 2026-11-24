from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2RouteServerBgpStatus(BaseModel):
    Status: StrictStr | None = None
