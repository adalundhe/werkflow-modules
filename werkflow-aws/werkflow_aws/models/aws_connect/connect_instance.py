from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .connect_instance_status_reason import ConnectInstanceStatusReason


class ConnectInstance(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    IdentityManagementType: StrictStr | None = None
    InstanceAlias: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    ServiceRole: StrictStr | None = None
    InstanceStatus: StrictStr | None = None
    StatusReason: ConnectInstanceStatusReason | None = None
    InboundCallsEnabled: StrictBool | None = None
    OutboundCallsEnabled: StrictBool | None = None
    InstanceAccessUrl: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
