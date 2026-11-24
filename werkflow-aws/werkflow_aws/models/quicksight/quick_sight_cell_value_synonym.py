from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightCellValueSynonym(BaseModel):
    CellValue: StrictStr | None = None
    Synonyms: list[StrictStr] | None = None
