from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystFilter(BaseModel):
    key: StrictStr
    values: list[StrictStr]
    comparisonOperator: StrictStr | None = None
