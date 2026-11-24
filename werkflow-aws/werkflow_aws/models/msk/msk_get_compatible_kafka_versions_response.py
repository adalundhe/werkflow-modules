from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .msk_compatible_kafka_version import MSKCompatibleKafkaVersion


class MSKGetCompatibleKafkaVersionsResponse(BaseModel):
    CompatibleKafkaVersions: list[MSKCompatibleKafkaVersion] | None = None
    ResponseMetadata: dict[str, Any] | None = None
