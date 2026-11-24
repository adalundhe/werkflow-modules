from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DetectiveNewAsoDetail(BaseModel):
    Aso: StrictStr | None = None
    IsNewForEntireAccount: StrictBool | None = None
