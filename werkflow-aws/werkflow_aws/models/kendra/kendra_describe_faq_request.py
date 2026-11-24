from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraDescribeFaqRequest(BaseModel):
    Id: StrictStr
    IndexId: StrictStr
