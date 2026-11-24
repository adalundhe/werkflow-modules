from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class EC2NetworkCardInfo(BaseModel):
    NetworkCardIndex: StrictInt | None = None
    NetworkPerformance: StrictStr | None = None
    MaximumNetworkInterfaces: StrictInt | None = None
    AdditionalFlexibleNetworkInterfaces: StrictInt | None = None
    BaselineBandwidthInGbps: StrictFloat | StrictInt | None = None
    PeakBandwidthInGbps: StrictFloat | StrictInt | None = None
    DefaultEnaQueueCountPerInterface: StrictInt | None = None
    MaximumEnaQueueCount: StrictInt | None = None
    MaximumEnaQueueCountPerInterface: StrictInt | None = None
    InterfaceTypes: list[StrictStr] | None = None
