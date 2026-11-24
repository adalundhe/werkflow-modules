from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2DescribeByoipCidrsRequest(BaseModel):
    MaxResults: StrictInt
    DryRun: StrictBool | None = None
    NextToken: StrictStr | None = None
