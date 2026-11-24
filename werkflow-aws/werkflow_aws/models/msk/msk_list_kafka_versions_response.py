from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .msk_kafka_version import MSKKafkaVersion


class MSKListKafkaVersionsResponse(BaseModel):
    KafkaVersions: list[MSKKafkaVersion] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
