from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .mq_data_replication_counterpart import MQDataReplicationCounterpart


class MQDataReplicationMetadataOutput(BaseModel):
    DataReplicationCounterpart: MQDataReplicationCounterpart | None = None
    DataReplicationRole: StrictStr | None = None
