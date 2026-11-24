from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DocumentDBDeleteDBInstanceRequest(BaseModel):
    DBInstanceIdentifier: StrictStr
