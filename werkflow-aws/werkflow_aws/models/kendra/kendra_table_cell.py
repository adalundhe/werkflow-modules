from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class KendraTableCell(BaseModel):
    Value: StrictStr | None = None
    TopAnswer: StrictBool | None = None
    Highlighted: StrictBool | None = None
    Header: StrictBool | None = None
