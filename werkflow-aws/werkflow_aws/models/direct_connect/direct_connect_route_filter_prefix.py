from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectRouteFilterPrefix(BaseModel):
    cidr: StrictStr | None = None
