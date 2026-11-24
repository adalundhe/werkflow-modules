from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraDeleteDataSourceRequest(BaseModel):
    Id: StrictStr
    IndexId: StrictStr
