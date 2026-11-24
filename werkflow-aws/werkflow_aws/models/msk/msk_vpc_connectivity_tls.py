from __future__ import annotations
from pydantic import BaseModel, StrictBool


class MSKVpcConnectivityTls(BaseModel):
    Enabled: StrictBool | None = None
