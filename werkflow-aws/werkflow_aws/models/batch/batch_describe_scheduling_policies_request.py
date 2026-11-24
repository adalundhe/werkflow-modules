from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchDescribeSchedulingPoliciesRequest(BaseModel):
    arns: list[StrictStr]
