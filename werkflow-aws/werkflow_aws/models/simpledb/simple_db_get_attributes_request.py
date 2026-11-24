from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SimpleDBGetAttributesRequest(BaseModel):
    DomainName: StrictStr
    ItemName: StrictStr
    AttributeNames: list[StrictStr] | None = None
    ConsistentRead: StrictBool | None = None
