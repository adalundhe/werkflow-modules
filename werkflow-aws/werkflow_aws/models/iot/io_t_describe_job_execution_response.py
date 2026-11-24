from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .io_t_job_execution import IoTJobExecution


class IoTDescribeJobExecutionResponse(BaseModel):
    execution: IoTJobExecution | None = None
    ResponseMetadata: dict[str, Any] | None = None
