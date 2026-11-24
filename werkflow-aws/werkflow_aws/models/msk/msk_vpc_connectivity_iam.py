from __future__ import annotations
from pydantic import BaseModel, StrictBool


class MSKVpcConnectivityIam(BaseModel):
    Enabled: StrictBool | None = None
