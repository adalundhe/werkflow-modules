from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMInstanceInfo(BaseModel):
    AgentType: StrictStr | None = None
    AgentVersion: StrictStr | None = None
    ComputerName: StrictStr | None = None
    InstanceStatus: StrictStr | None = None
    IpAddress: StrictStr | None = None
    ManagedStatus: StrictStr | None = None
    Name: StrictStr | None = None
    PlatformType: StrictStr | None = None
    PlatformName: StrictStr | None = None
    PlatformVersion: StrictStr | None = None
    ResourceType: StrictStr | None = None
    SourceType: StrictStr | None = None
    SourceId: StrictStr | None = None
    SourceLocation: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
