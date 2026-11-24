from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DataPipelineDescribeObjectsRequest(BaseModel):
    pipelineId: StrictStr
    objectIds: list[StrictStr]
    evaluateExpressions: StrictBool | None = None
    marker: StrictStr | None = None
