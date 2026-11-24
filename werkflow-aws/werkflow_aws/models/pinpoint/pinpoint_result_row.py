from __future__ import annotations
from pydantic import BaseModel
from .pinpoint_result_row_value import PinpointResultRowValue


class PinpointResultRow(BaseModel):
    GroupedBys: list[PinpointResultRowValue] | None = None
    Values: list[PinpointResultRowValue] | None = None
