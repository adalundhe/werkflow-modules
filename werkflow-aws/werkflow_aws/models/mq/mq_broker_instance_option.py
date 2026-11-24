from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .mq_availability_zone import MQAvailabilityZone


class MQBrokerInstanceOption(BaseModel):
    AvailabilityZones: list[MQAvailabilityZone] | None = None
    EngineType: StrictStr | None = None
    HostInstanceType: StrictStr | None = None
    StorageType: StrictStr | None = None
    SupportedDeploymentModes: list[StrictStr] | None = None
    SupportedEngineVersions: list[StrictStr] | None = None
