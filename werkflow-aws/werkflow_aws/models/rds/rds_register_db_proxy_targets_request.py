from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSRegisterDBProxyTargetsRequest(BaseModel):
    DBProxyName: StrictStr
    TargetGroupName: StrictStr | None = None
    DBInstanceIdentifiers: list[StrictStr] | None = None
    DBClusterIdentifiers: list[StrictStr] | None = None
