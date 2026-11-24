from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyVpcEndpointConnectionNotificationRequest(BaseModel):
    ConnectionNotificationId: StrictStr
    DryRun: StrictBool | None = None
    ConnectionNotificationArn: StrictStr | None = None
    ConnectionEvents: list[StrictStr] | None = None
