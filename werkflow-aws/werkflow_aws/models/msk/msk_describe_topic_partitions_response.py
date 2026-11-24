from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .msk_topic_partition_info import MSKTopicPartitionInfo


class MSKDescribeTopicPartitionsResponse(BaseModel):
    Partitions: list[MSKTopicPartitionInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
