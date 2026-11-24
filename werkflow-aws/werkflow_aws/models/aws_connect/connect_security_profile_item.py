from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectSecurityProfileItem(BaseModel):
    Id: StrictStr | None = None
