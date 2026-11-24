from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightFilterListConfiguration(BaseModel):
    MatchOperator: StrictStr | None = None
    CategoryValues: list[StrictStr] | None = None
    SelectAllOptions: StrictStr | None = None
    NullOption: StrictStr | None = None
