from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_output_column_name_override import QuickSightOutputColumnNameOverride


class QuickSightJoinOperandProperties(BaseModel):
    OutputColumnNameOverrides: list[QuickSightOutputColumnNameOverride] | None = None
