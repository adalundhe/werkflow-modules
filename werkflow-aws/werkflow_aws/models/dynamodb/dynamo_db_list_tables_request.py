from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DynamoDBListTablesRequest(BaseModel):
    ExclusiveStartTableName: StrictStr | None = None
    Limit: StrictInt | None = None
