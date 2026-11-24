from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraDeleteIndexRequest(BaseModel):
    Id: StrictStr
