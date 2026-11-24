from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class NeptuneRebootDBInstanceRequest(BaseModel):
    DBInstanceIdentifier: StrictStr
    ForceFailover: StrictBool | None = None
