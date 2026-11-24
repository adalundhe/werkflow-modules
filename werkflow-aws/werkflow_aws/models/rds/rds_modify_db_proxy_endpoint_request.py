from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSModifyDBProxyEndpointRequest(BaseModel):
    DBProxyEndpointName: StrictStr
    NewDBProxyEndpointName: StrictStr | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
