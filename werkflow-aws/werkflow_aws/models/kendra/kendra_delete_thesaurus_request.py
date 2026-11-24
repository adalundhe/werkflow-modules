from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraDeleteThesaurusRequest(BaseModel):
    Id: StrictStr
    IndexId: StrictStr
