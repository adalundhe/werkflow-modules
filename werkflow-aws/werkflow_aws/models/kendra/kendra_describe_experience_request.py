from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraDescribeExperienceRequest(BaseModel):
    Id: StrictStr
    IndexId: StrictStr
