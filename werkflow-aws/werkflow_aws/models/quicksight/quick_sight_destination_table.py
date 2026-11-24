from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_destination_table_source import QuickSightDestinationTableSource


class QuickSightDestinationTable(BaseModel):
    Alias: StrictStr | None = None
    Source: QuickSightDestinationTableSource | None = None
