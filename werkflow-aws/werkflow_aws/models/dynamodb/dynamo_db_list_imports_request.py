from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DynamoDBListImportsRequest(BaseModel):
    TableArn: StrictStr | None = None
    PageSize: StrictInt | None = None
    NextToken: StrictStr | None = None
