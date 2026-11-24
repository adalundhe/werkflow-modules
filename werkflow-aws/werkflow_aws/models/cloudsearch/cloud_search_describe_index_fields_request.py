from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudSearchDescribeIndexFieldsRequest(BaseModel):
    DomainName: StrictStr
    FieldNames: list[StrictStr] | None = None
    Deployed: StrictBool | None = None
