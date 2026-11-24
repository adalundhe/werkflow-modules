from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DocumentDBRebootDBInstanceRequest(BaseModel):
    DBInstanceIdentifier: StrictStr
    ForceFailover: StrictBool | None = None
