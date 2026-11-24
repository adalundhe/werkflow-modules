from __future__ import annotations
from pydantic import BaseModel
from .firehose_partition_field import FirehosePartitionField


class FirehosePartitionSpec(BaseModel):
    Identity: list[FirehosePartitionField] | None = None
