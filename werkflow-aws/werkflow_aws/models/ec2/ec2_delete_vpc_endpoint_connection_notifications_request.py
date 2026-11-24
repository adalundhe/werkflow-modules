from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteVpcEndpointConnectionNotificationsRequest(BaseModel):
    ConnectionNotificationIds: list[StrictStr]
    DryRun: StrictBool | None = None
