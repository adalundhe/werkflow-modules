from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DynamoDBListGlobalTablesRequest(BaseModel):
    ExclusiveStartGlobalTableName: StrictStr | None = None
    Limit: StrictInt | None = None
    RegionName: StrictStr | None = None
