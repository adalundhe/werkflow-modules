from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class RDSRebootDBInstanceRequest(BaseModel):
    DBInstanceIdentifier: StrictStr
    ForceFailover: StrictBool | None = None
