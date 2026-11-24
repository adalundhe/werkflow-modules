from __future__ import annotations
from pydantic import BaseModel, StrictInt


class FMSNetworkAclPortRange(BaseModel):
    From: StrictInt | None = None
    To: StrictInt | None = None
