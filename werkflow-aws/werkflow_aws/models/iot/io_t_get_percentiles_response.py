from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .io_t_percent_pair import IoTPercentPair


class IoTGetPercentilesResponse(BaseModel):
    percentiles: list[IoTPercentPair] | None = None
    ResponseMetadata: dict[str, Any] | None = None
