from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ECSDescribeExpressGatewayServiceRequest(BaseModel):
    serviceArn: StrictStr
    include: list[Literal['TAGS']] | None = None
