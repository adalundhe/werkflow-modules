from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKDeleteReplicatorRequest(BaseModel):
    ReplicatorArn: StrictStr
    CurrentVersion: StrictStr | None = None
