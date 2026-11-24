from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_connection_pool_configuration import RDSConnectionPoolConfiguration


class RDSModifyDBProxyTargetGroupRequest(BaseModel):
    TargetGroupName: StrictStr
    DBProxyName: StrictStr
    ConnectionPoolConfig: RDSConnectionPoolConfiguration | None = None
    NewName: StrictStr | None = None
