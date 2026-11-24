from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_hours_of_operation import ConnectHoursOfOperation


class ConnectDescribeHoursOfOperationResponse(BaseModel):
    HoursOfOperation: ConnectHoursOfOperation | None = None
    ResponseMetadata: dict[str, Any] | None = None
