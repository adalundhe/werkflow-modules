from __future__ import annotations
from pydantic import BaseModel
from .kinesis_partition_field import KinesisPartitionField


class KinesisPartitionSpec(BaseModel):
    PartitionFields: list[KinesisPartitionField] | None = None
