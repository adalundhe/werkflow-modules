from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueBatchGetJobsRequest(BaseModel):
    JobNames: list[StrictStr]
