from __future__ import annotations
from pydantic import BaseModel, StrictBool


class RichText(BaseModel):
    empty: StrictBool | None = None
    emptyAdf: StrictBool | None = None
    finalised: StrictBool | None = None
    valueSet: StrictBool | None = None
