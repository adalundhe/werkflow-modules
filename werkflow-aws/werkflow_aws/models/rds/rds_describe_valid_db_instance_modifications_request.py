from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDescribeValidDBInstanceModificationsRequest(BaseModel):
    DBInstanceIdentifier: StrictStr
