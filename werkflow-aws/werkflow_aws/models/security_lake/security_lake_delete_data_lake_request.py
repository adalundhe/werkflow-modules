from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityLakeDeleteDataLakeRequest(BaseModel):
    regions: list[StrictStr]
