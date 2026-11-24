from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueBatchGetWorkflowsRequest(BaseModel):
    Names: list[StrictStr]
    IncludeGraph: StrictBool | None = None
