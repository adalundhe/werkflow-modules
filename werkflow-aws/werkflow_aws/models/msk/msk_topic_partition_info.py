from __future__ import annotations
from pydantic import BaseModel, StrictInt


class MSKTopicPartitionInfo(BaseModel):
    Partition: StrictInt | None = None
    Leader: StrictInt | None = None
    Replicas: list[StrictInt] | None = None
    Isr: list[StrictInt] | None = None
