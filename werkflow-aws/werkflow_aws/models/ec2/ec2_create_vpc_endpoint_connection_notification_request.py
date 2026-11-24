from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2CreateVpcEndpointConnectionNotificationRequest(BaseModel):
    ConnectionNotificationArn: StrictStr
    ConnectionEvents: list[StrictStr]
    DryRun: StrictBool | None = None
    ServiceId: StrictStr | None = None
    VpcEndpointId: StrictStr | None = None
    ClientToken: StrictStr | None = None
