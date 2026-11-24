from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .batch_service_environment_detail import BatchServiceEnvironmentDetail


class BatchDescribeServiceEnvironmentsResponse(BaseModel):
    serviceEnvironments: list[BatchServiceEnvironmentDetail] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
