from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DescribeSecurityGroupReferencesRequest(BaseModel):
    GroupId: list[StrictStr]
    DryRun: StrictBool | None = None
