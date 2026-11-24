from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_cross_channel_behavior import ConnectCrossChannelBehavior
from .connect_workload_type_concurrency import ConnectWorkloadTypeConcurrency


class ConnectMediaConcurrency(BaseModel):
    Channel: StrictStr | None = None
    Concurrency: StrictInt | None = None
    CrossChannelBehavior: ConnectCrossChannelBehavior | None = None
    WorkloadTypeConcurrencies: list[ConnectWorkloadTypeConcurrency] | None = None
