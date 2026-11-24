from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .quick_sight_network_interface import QuickSightNetworkInterface


class QuickSightVPCConnectionSummary(BaseModel):
    VPCConnectionId: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    VPCId: StrictStr | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    DnsResolvers: list[StrictStr] | None = None
    Status: StrictStr | None = None
    AvailabilityStatus: StrictStr | None = None
    NetworkInterfaces: list[QuickSightNetworkInterface] | None = None
    RoleArn: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
