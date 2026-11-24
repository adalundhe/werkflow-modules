from __future__ import annotations
from pydantic import BaseModel, StrictBool


class GlueNullCheckBoxList(BaseModel):
    IsEmpty: StrictBool | None = None
    IsNullString: StrictBool | None = None
    IsNegOne: StrictBool | None = None
