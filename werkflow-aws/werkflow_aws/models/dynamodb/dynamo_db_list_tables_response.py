from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBListTablesResponse(BaseModel):
    TableNames: list[StrictStr] | None = None
    LastEvaluatedTableName: StrictStr | None = None
