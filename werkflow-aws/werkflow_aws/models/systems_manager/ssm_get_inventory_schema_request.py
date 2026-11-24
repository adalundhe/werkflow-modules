from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SSMGetInventorySchemaRequest(BaseModel):
    TypeName: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    Aggregator: StrictBool | None = None
    SubType: StrictBool | None = None
