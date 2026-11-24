from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2DescribeIdFormatRequest(BaseModel):
    Resource: StrictStr | None = None
