from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class GuardDutyInvestigationEc2Instance(BaseModel):
    InstanceId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    InstanceState: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    PrivateIpAddress: StrictStr | None = None
    PublicIp: StrictStr | None = None
    VpcId: StrictStr | None = None
    SubnetId: StrictStr | None = None
    ImageId: StrictStr | None = None
    LaunchedAt: datetime.datetime | StrictStr | None = None
