from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NeptuneDescribeValidDBInstanceModificationsRequest(BaseModel):
    DBInstanceIdentifier: StrictStr
