from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class PinpointEmailChannelRequest(BaseModel):
    FromAddress: StrictStr
    Identity: StrictStr
    ConfigurationSet: StrictStr | None = None
    Enabled: StrictBool | None = None
    RoleArn: StrictStr | None = None
    OrchestrationSendingRoleArn: StrictStr | None = None
