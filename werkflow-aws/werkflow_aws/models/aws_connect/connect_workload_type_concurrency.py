from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_cross_channel_workload_behavior import ConnectCrossChannelWorkloadBehavior


class ConnectWorkloadTypeConcurrency(BaseModel):
    WorkloadType: StrictStr | None = None
    Concurrency: StrictInt | None = None
    CrossChannelWorkloadBehavior: ConnectCrossChannelWorkloadBehavior | None = None
