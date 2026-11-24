from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class ConnectCreateInstanceRequest(BaseModel):
    IdentityManagementType: Literal['SAML', 'CONNECT_MANAGED', 'EXISTING_DIRECTORY']
    InboundCallsEnabled: StrictBool
    OutboundCallsEnabled: StrictBool
    ClientToken: StrictStr | None = None
    InstanceAlias: StrictStr | None = None
    DirectoryId: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
