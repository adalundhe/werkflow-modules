from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_hours_of_operation_override import ConnectHoursOfOperationOverride


class ConnectDescribeHoursOfOperationOverrideResponse(BaseModel):
    HoursOfOperationOverride: ConnectHoursOfOperationOverride | None = None
    ResponseMetadata: dict[str, Any] | None = None
