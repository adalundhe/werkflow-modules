from __future__ import annotations
from pydantic import BaseModel
from .pinpoint_result_row import PinpointResultRow


class PinpointBaseKpiResult(BaseModel):
    Rows: list[PinpointResultRow] | None = None
