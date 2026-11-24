from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .device_farm_job import DeviceFarmJob


class DeviceFarmListJobsResponse(BaseModel):
    jobs: list[DeviceFarmJob] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
