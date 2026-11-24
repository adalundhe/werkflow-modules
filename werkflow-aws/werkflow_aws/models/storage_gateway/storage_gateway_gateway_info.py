from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayGatewayInfo(BaseModel):
    GatewayId: StrictStr | None = None
    GatewayARN: StrictStr | None = None
    GatewayType: StrictStr | None = None
    GatewayOperationalState: StrictStr | None = None
    GatewayName: StrictStr | None = None
    Ec2InstanceId: StrictStr | None = None
    Ec2InstanceRegion: StrictStr | None = None
    HostEnvironment: StrictStr | None = None
    HostEnvironmentId: StrictStr | None = None
    DeprecationDate: StrictStr | None = None
    SoftwareVersion: StrictStr | None = None
