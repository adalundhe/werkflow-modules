from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamDescribeStacksRequest(BaseModel):
    Names: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
