from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_connection_notification import EC2ConnectionNotification


class EC2CreateVpcEndpointConnectionNotificationResponse(BaseModel):
    ConnectionNotification: EC2ConnectionNotification | None = None
    ClientToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
