from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudSearchDescribeExpressionsRequest(BaseModel):
    DomainName: StrictStr
    ExpressionNames: list[StrictStr] | None = None
    Deployed: StrictBool | None = None
