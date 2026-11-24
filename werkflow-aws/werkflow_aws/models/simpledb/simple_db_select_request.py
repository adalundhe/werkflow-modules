from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SimpleDBSelectRequest(BaseModel):
    SelectExpression: StrictStr
    NextToken: StrictStr | None = None
    ConsistentRead: StrictBool | None = None
