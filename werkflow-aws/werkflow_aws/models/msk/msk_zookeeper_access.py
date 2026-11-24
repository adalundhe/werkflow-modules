from __future__ import annotations
from pydantic import BaseModel, StrictBool


class MSKZookeeperAccess(BaseModel):
    Enabled: StrictBool | None = None
