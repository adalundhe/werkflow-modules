from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightCustomFilterConfiguration(BaseModel):
    MatchOperator: StrictStr | None = None
    CategoryValue: StrictStr | None = None
    SelectAllOptions: StrictStr | None = None
    ParameterName: StrictStr | None = None
    NullOption: StrictStr | None = None
