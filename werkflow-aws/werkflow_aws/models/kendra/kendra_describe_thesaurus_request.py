from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraDescribeThesaurusRequest(BaseModel):
    Id: StrictStr
    IndexId: StrictStr
