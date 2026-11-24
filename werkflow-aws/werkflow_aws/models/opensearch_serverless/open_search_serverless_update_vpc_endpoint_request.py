from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessUpdateVpcEndpointRequest(BaseModel):
    id: StrictStr
    addSubnetIds: list[StrictStr] | None = None
    removeSubnetIds: list[StrictStr] | None = None
    addSecurityGroupIds: list[StrictStr] | None = None
    removeSecurityGroupIds: list[StrictStr] | None = None
    clientToken: StrictStr | None = None
