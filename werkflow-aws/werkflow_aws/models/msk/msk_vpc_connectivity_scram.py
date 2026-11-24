from __future__ import annotations
from pydantic import BaseModel, StrictBool


class MSKVpcConnectivityScram(BaseModel):
    Enabled: StrictBool | None = None
