from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraDeleteFaqRequest(BaseModel):
    Id: StrictStr
    IndexId: StrictStr
