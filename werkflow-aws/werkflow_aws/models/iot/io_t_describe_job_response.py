from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_job import IoTJob


class IoTDescribeJobResponse(BaseModel):
    documentSource: StrictStr | None = None
    job: IoTJob | None = None
    ResponseMetadata: dict[str, Any] | None = None
