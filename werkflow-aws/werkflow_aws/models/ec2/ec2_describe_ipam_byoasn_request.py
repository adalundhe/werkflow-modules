from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2DescribeIpamByoasnRequest(BaseModel):
    DryRun: StrictBool | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
