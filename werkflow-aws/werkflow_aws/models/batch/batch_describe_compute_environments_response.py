from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .batch_compute_environment_detail import BatchComputeEnvironmentDetail


class BatchDescribeComputeEnvironmentsResponse(BaseModel):
    computeEnvironments: list[BatchComputeEnvironmentDetail] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
