from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKDescribeVpcConnectionRequest(BaseModel):
    Arn: StrictStr
