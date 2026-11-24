from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DescribeConversionTasksRequest(BaseModel):
    DryRun: StrictBool | None = None
    ConversionTaskIds: list[StrictStr] | None = None
